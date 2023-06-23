from contextlib import contextmanager
from typing import Generator, List
from mongoengine import connect, disconnect
from infrastructure.models import WeatherData
from infrastructure.config import settings


class DbOperation:
    @contextmanager
    def create_mongo_connection(self) -> Generator:
        connection = connect(settings.db_name, host=settings.mongo_db_connection)
        try:
            yield connection
        finally:
            disconnect(connection)

    def migrate(self) -> None:
        with self.create_mongo_connection() as connection:
            if settings.db_name not in connection.list_database_names():
                connection[settings.db_name]  # Create the database if it does not exist
            WeatherData.create_index([("city", "text")])

    def query_weather_data(self, query=dict()) -> List[WeatherData]:
        with self.create_mongo_connection():
            return WeatherData.objects(**query).order_by("city", "region", "country").all()

    def store_weather_data(self, weather_data) -> None:
        with self.create_mongo_connection():
            weather_data.save()
