from simulation import simulate_weather
from visualization import plot_temperature_trend

def summarize_forecast(forecast):
    total_temp = sum([day['Temperature'] for day in forecast])
    total_humidity = sum([day['Humidity'] for day in forecast])
    max_temp = max([day['Temperature'] for day in forecast])
    min_temp = min([day['Temperature'] for day in forecast])

    avg_temp = total_temp / len(forecast)
    avg_humidity = total_humidity / len(forecast)

    weather_types = [day['Weather Type'] for day in forecast]
    sunny_days = weather_types.count('Sunny')
    rainy_days = weather_types.count('Rainy')
    snowy_days = weather_types.count('Snowy')
    cloudy_days = weather_types.count('Cloudy')

    forecast_summary = f"""
Forecast Summary:
Average Temperature: {avg_temp:.2f}°C
Average Humidity: {avg_humidity:.2f}%
Max Temperature: {max_temp:.2f}°C
Min Temperature: {min_temp:.2f}°C
Sunny Days: {sunny_days}
Rainy Days: {rainy_days}
Snowy Days: {snowy_days}
Cloudy Days: {cloudy_days}
"""
    print(forecast_summary)
    return forecast_summary

def main():
    days = int(input("Enter the number of days to simulate: "))
    season = input("Enter the season (Summer, Winter, Spring, Autumn): ").capitalize()

    try:
        forecast = simulate_weather(days, season)

        for i, day in enumerate(forecast, start=1):
            print(f"Day {i}: {day}")

        plot_temperature_trend(forecast)

        summarize_forecast(forecast)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()