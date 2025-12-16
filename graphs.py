import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
data = pd.read_csv(BASE_DIR / 'initial_conditions.txt')

# Rename columns safely
data.columns = ['distance', 'concentration']

distance = data['distance'].values
concentration = data['concentration'].values


# Define timestep manually (seconds)
timestep = 1.0

# Create fake time evolution
time_snapshots = 10
concentration_data = np.tile(concentration, (time_snapshots, 1))



def plot_snapshots(data, spatial_grid, time_step, snapshots=8,
                   graph_title='Initial conditions'):
    total_steps = data.shape[0]
    step_interval = max(total_steps // snapshots, 1)

    plt.figure(figsize=(10, 5))
    for step in range(0, total_steps, step_interval):
        plt.plot(spatial_grid, data[step],
                 label=f'Time = {step * time_step:.0f} s')

    plt.xlabel('Distance (m)')
    plt.ylabel('Concentration (μg/m³)')
    plt.title(graph_title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()





def plot_concentration_heatmap(data, distance_range, timestep,
                               heatmap_title='Concentration Over Time'):
    plt.figure(figsize=(10, 6))
    plt.imshow(
        data,
        aspect='auto',
        extent=[distance_range[0], distance_range[-1],
                data.shape[0] * timestep, 0],
        cmap='coolwarm'
    )
    plt.colorbar(label='Concentration (μg/m³)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Time (s)')
    plt.title(heatmap_title)
    plt.tight_layout()
    plt.show()

# ---------- Run plots ----------


simulation_2 = concentration_data

simulations = {

    "Simulation 2": simulation_2,
}

plot_snapshots(concentration_data, distance, timestep)
plot_concentration_heatmap(concentration_data, distance, timestep)
