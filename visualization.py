import matplotlib.pyplot as plt

def plot_temperature_trend(forecast):
    temperatures = [day['Temperature'] for day in forecast]
    days = list(range(1, len(forecast) + 1))

    plt.figure(figsize=(10, 5))
    plt.plot(days, temperatures, marker='o', label='Temperature (°C)')
    plt.title('Temperature Trend')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid()
    plt.show()