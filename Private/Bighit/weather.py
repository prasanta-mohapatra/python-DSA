import argparse
import logging
from typing import List, Optional
import requests
import json
from rich.console import Console
from rich.table import Table
from infrastructure.config import settings
from infrastructure.operation import DbOperation
from infrastructure.models import WeatherData


def fetch_weather_data(city: str) -> Optional[WeatherData]:
    """
    Fetch the weather data from API.

    Parameters
    ----------
    city: str
        City Name.

    Returns
    -------
    WeatherData
        Weather Data.

    """
    url = f"http://api.weatherapi.com/v1/current.json?key={settings.weather_api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return WeatherData.from_data(response.json())
    else:
        print("Failed to fetch weather data.")
        return


def display_weather_data(weather_data: List[WeatherData]) -> None:
    """
    Display the weather data in table.

    Parameters
    ----------
    weather_data: List[WeatherData]
        Weather Data.

    Returns
    -------
    None

    """
    if not weather_data:
        print("No weather data available.")
        return

    table = Table(title="Weather Data")
    table.add_column("City")
    table.add_column("Region")
    table.add_column("Country")
    table.add_column("Temperature")
    table.add_column("Humidity")
    table.add_column("Wind Speed")
    table.add_column("Wind Direction")
    table.add_column("Pressure")
    table.add_column("Localtime")
    table.add_column("Location")
    table.add_column("Timezone")

    for data in weather_data:
        table.add_row(
            str(data.city),
            str(data.region),
            str(data.country),
            str(data.temperature),
            str(data.humidity),
            str(data.wind_speed),
            str(data.wind_direction),
            str(data.pressure),
            str(data.localtime),
            str(data.location),
            str(data.timezone),
        )

    console = Console()
    console.print(table)


def main() -> None:
    """
    Main Function.

    Returns
    -------
    None

    """
    parser = argparse.ArgumentParser(description="Fetch and store weather data")
    parser.add_argument("--city", type=str, help="City name")
    parser.add_argument(
        "--query", type=str, help="Query and display stored weather data", default="{}"
    )
    args = parser.parse_args()

    db_operation = DbOperation()
    db_operation.migrate()
    try:
        query = json.loads(args.query.replace("'", '"'))
    except Exception as ex:
        logging.exception(ex)
        query = {}

    if not args.city:
        db_data = db_operation.query_weather_data(query)
        display_weather_data(db_data)
        exit()

    weather_data = fetch_weather_data(args.city)
    logging.info("Weather data fetched succesfully")
    if weather_data:
        db_operation.store_weather_data(weather_data)
        logging.info(f"Weather data of {args.city} inserted in Database")


if __name__ == "__main__":
    main()
