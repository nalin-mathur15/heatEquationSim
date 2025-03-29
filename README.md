# Heat Equation Simulation

This project provides a user-friendly graphical interface for simulating the 1D heat equation using finite difference methods. Users can dynamically modify parameters such as initial conditions, boundary conditions, and numerical settings to observe how heat propagates over time.

## Features
- **Polynomial-based Initial Condition**: Users can input any polynomial function to define the starting temperature distribution.
- **Boundary Condition Control**: Users can set fixed boundary values at both ends of the domain.
- **Dynamic Parameter Adjustments**: Adjustable parameters:
  - Thermal diffusivity (`alpha`)
  - Grid points (`nx`)
  - Spatial step (`dx`)
  - Time step (`dt`)
  - Number of time steps (`time_steps`)
- **Real-time Visualisation**: An animated plot displays how temperature evolves over time.

## Requirements
Ensure you have the following Python libraries installed:
```sh
pip install numpy matplotlib sympy tkinter
```

## Usage
Run the script using:
```sh
python heateqn.py
```
### Steps:
1. Enter a polynomial function for the initial condition (e.g., `x**2 - 2*x`).
2. Adjust numerical parameters using sliders.
3. Set left and right boundary conditions.
4. Click "Run Simulation" to visualise the heat propagation.
5. Click "Quit" to close the application.

## How It Works
The simulation uses an explicit finite difference scheme to numerically solve the 1D heat equation:

$u_{t+1}(x) = u_t(x) + \alpha \frac{dt}{dx^2} (u_t(x+dx) - 2u_t(x) + u_t(x-dx))$

## Future Improvements
- Extend to 2D simulations.
- Allow different types of boundary conditions (e.g., Neumann conditions).
- Allow non-polynomial initial condition.
- Improve computational efficiency with implicit methods.

