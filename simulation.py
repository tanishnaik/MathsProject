from weather import generate_weather

def simulate_weather(days, season):
    if season not in ["Summer", "Winter", "Spring", "Autumn"]:
        raise ValueError("Invalid season! Choose from Summer, Winter, Spring, or Autumn.")

    return [generate_weather(season) for _ in range(days)]