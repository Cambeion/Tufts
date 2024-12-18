import csv
import matplotlib.pyplot as plt

# Initialize lists for time and temperature
time_elapsed = []
sensor1_temps = []

# Open and read the CSV file
with open('temperature_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        time_elapsed.append(float(row[0]))
        sensor1_temps.append(float(row[1]))
    
# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time_elapsed, sensor1_temps, label='Sensor 1 (°F)', color='red', marker='o')

# Add labels, title, and legend
plt.xlabel('Time Elapsed (s)', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.title('Temperature Data Over Time', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)

# Improve layout and display the plot
plt.tight_layout()
plt.show()

# Show the plot
plt.tight_layout()
plt.show()
