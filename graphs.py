import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data into a pandas DataFrame
data = pd.read_csv('initial_conditions.txt', delim_whitespace=True)

# Access `distance` and `concentration` directly
distance = data['distance']
concentration = data['concentration']

# Verify the data
print("Distance:\n", distance)
print("Concentration:\n", concentration)

# Use directly in your code
spatial_grid = distance
time_step = 1  # Default time step of 1 second

# Visualize using your `plot_snapshots` function
plot_snapshots(data=[concentration], spatial_grid=spatial_grid, time_step=time_step)
# Function to visualize pollutant concentration at several time intervals
# Parameters:
#   data: 2D array(time, space)
#   spatial_grid: 1D array representing distances
#   time_step: timestep in seconds
#   snapshots: number of time intervals to display
def plot_snapshots(data, spatial_grid, time_step, snapshots=8, graph_title='Pollutant Spread Over Time'):
    total_steps = data.shape[0]
    step_interval = max(total_steps // snapshots, 1)

    plt.figure(figsize=(10, 5))

    for step in range(0, total_steps, step_interval):
        plt.plot(spatial_grid, data[step], label=f'Time = {step * time_step:.0f} s')

    plt.xlabel('Distance (m)')
    plt.ylabel('Concentration (μg/m³)')
    plt.title(graph_title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
# Function to compare multiple simulation results in one plot
# Parameters:
#   simulations: dictionary of {'label': 2D data array}
#   distance_grid: spatial grid representing model distance
#   dt: simulation timestep in seconds
def compare_simulations(simulations, distance_grid, dt):
    plt.figure(figsize=(10, 5))

    for name, data in simulations.items():
        plt.plot(distance_grid, data[-1], label=f'{name} (final t={data.shape[0] * dt}s)')

    plt.xlabel('Distance (m)')
    plt.ylabel('Concentration (μg/m³)')
    plt.title('Comparison of Simulation Results')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function to create a heatmap of concentration over time
# Parameters:
#   data: 2D array(time, space)
#   distance_range: spatial grid
#   timestep: time interval in seconds
def plot_concentration_heatmap(data, distance_range, timestep, heatmap_title='Concentration Over Time (Heatmap)'):
    plt.figure(figsize=(10, 6))

    plt.imshow(data, aspect='auto', extent=[distance_range[0], distance_range[-1], data.shape[0] * timestep, 0], cmap='coolwarm')

    plt.colorbar(label='Concentration (μg/m³)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Time (s)')
    plt.title(heatmap_title)
    plt.tight_layout()
    plt.show()
