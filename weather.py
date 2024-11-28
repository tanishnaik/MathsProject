import random

def generate_weather(season):
    base_temp = {"Summer": 30, "Winter": 0, "Spring": 15, "Autumn": 10}
    base_humidity = {"Summer": 50, "Winter": 30, "Spring": 60, "Autumn": 70}

    temperature = base_temp[season] + random.uniform(-5, 5)
    humidity = base_humidity[season] + random.randint(-10, 10)
    wind_speed = random.uniform(0, 20)

    weather_types = {
        "Summer": ["Sunny", "Cloudy"],
        "Winter": ["Snowy", "Cloudy"],
        "Spring": ["Rainy", "Sunny", "Cloudy"],
        "Autumn": ["Rainy", "Cloudy"]
    }

    weather_type = random.choice(weather_types[season])

    return {
        "Temperature": round(temperature, 2),
        "Humidity": max(0, min(100, humidity)),
        "Wind Speed": round(wind_speed, 2),
        "Weather Type": weather_type
    }