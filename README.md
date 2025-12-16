# CNM_2025_group_03

### Project Overview

This project simulates the transport and evolution of a pollutant concentration in a river using numerical methods. The model computes pollutant concentration as a function of both time and distance along the river.

### Model Description

Pollutant transport is modelled using the one-dimensional advection equation:

### $$\frac{\partial \theta}{\partial t} = -U \frac{\partial \theta}{\partial x}$$


where:
- θ is the pollutant concentration (µg/m³)
- t is time (s)
- x is distance along the river (m)
- U is the flow velocity (m s⁻¹)

### Code Functionality
The code allows the user to define the model domain, spatial and temporal resolution, and flow velocity. It constructs the computational grid and solves the one-dimensional advection equation to simulate pollutant transport over time. Initial conditions can be specified directly or read from initial_conditions.csv, with the input data interpolated onto the model grid if required. Boundary conditions are applied at the edges of the domain, and the model produces plots to visualise how pollutant concentration evolves in space and time.

### Repository Structure
### Branch Structure
### How to run code
