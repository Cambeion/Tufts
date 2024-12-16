import csv
import matplotlib.pyplot as plt

# Read data from CSV file
time_elapsed = []
sensor1_temps = []
sensor2_temps = []

with open('temperature_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        time_elapsed.append(float(row[0]))
        sensor1_temps.append(float(row[1]))
        sensor2_temps.append(float(row[2]))

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time_elapsed, sensor1_temps, label='Sensor 1 (°F)', color='blue', marker='o')
plt.plot(time_elapsed, sensor2_temps, label='Sensor 2 (°F)', color='orange', marker='o')

# Add labels, title, and legend
plt.xlabel('Time Elapsed (s)', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.title('Temperature Data Over Time', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
