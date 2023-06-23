from mongoengine import Document, StringField, FloatField, IntField, DateTimeField, DictField


class WeatherData(Document):
    city = StringField(required=True)
    region = StringField(required=True)
    country = StringField(required=True)
    location = DictField()
    timezone = StringField()
    temperature = FloatField()
    humidity = IntField()
    wind_speed = FloatField()
    wind_direction = StringField()
    pressure = FloatField()
    localtime = DateTimeField(required=True)
    last_updated = DateTimeField(required=True)

    @classmethod
    def from_data(cls, data):
        location = data["location"]
        current = data["current"]

        return cls(
            city=location["name"],
            region=location["region"],
            country=location["country"],
            location={"latitude": location["lat"], "longitude": location["lon"]},
            timezone=location["tz_id"],
            temperature=current["temp_c"],
            humidity=current["humidity"],
            wind_speed=current["wind_kph"],
            wind_direction=current["wind_dir"],
            pressure=current["pressure_mb"],
            localtime=location["localtime"],
            last_updated=current["last_updated"],
        )
