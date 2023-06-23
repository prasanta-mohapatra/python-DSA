# Weather Data Fetcher

This code fetches weather data from a public API and stores it in a MongoDB database. It also provides a command-line interface to query and display the fetched weather data.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.x
- MongoDB
- Required Python packages (specified in requirements.txt)

## Installation

Install the required Python packages by running the following command:

```bash
pip install -r requirements.txt
```

Make sure MongoDB is installed and running.

## Usage

The code provides the following command-line options:

- `--city`: Specify the name of the city to fetch weather data for.
- `--query`: Query and display stored weather data.

To fetch and store weather data:

```bash
python weather.py --city <city_name>
```

Replace `<city_name>` with the name of the city you want to fetch weather data for.

To query and display stored weather data:

```bash
python weather.py --query <query_json>
```

Replace `<query_json>` with a JSON string representing the query. If no query is provided, all stored weather data will be displayed.

## Examples

Fetch and store weather data for a specific city:

```bash
python weather.py --city "Bengaluru"
```

Query and display stored weather data:

```bash
python weather.py --query "{'city':'Bengaluru'}"
```

## Notes

- Weather data is fetched from a public API (weatherapi.com) using the provided API key. Make sure you have a valid API key in the `settings.py` file.
- The fetched weather data is stored in a `MongoDB` database. Make sure you have `MongoDB` installed and running, and configure the database connection settings in the `settings.py` file.
