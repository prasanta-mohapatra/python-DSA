class Settings:
    weather_api_key: str = "41f8008de8764944bea65248232206"
    default_weather_city: str = "Bhubaneswar"
    db_host: str = "localhost"
    db_port: int = 27017
    db_name: str = "weather"

    @property
    def mongo_db_connection(self) -> str:
        return f"mongodb://{self.db_host}:{self.db_port}/"


settings = Settings()
