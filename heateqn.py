import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sympy as sp
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def initialCond(polynomialstr, nx, dx):
    x = sp.symbols('x')
    try:
        polynomial = sp.sympify(polynomialstr)
        x_vals = np.linspace(0, dx*(nx-1), nx)
        u0 = np.array([float(polynomial.subs(x, val)) for val in x_vals])
    except (sp.SympifyError, TypeError):
        u0 = np.zeros(nx)
    return u0
    
def heatEqn1D(u0, a, dx, dt, n):
    nx = len(u0)
    u = np.zeros((n, nx))
    u[0, :] = u0

    for i in range(1, n):
        for j in range(1, nx - 1):
            u[i, j] = u[i - 1, j] + a * (dt / dx**2) * (u[i - 1, j + 1] - 2 * u[i - 1, j] + u[i - 1, j - 1])
  
    return u

def animate1D(u, dx, dt):
    fig, ax = plt.subplots()
    line, = ax.plot(np.linspace(0, dx * (u.shape[1] - 1), u.shape[1]), u[0, :])

    def update(frame):
        line.set_ydata(u[frame, :])
        return line, 
  
    ani = animation.FuncAnimation(fig, update, frames = u.shape[0], interval = 150, blit = True)
    plt.xlabel("Position")
    plt.ylabel("Temperature")
    plt.title("1D Heat Equation")
    plt.show()
    
def runSim():
    def start_simulation():
        poly_str = poly_entry.get()
        alpha = float(alpha_var.get())
        nx = int(nx_var.get())
        dx = float(dx_var.get())
        dt = float(dt_var.get())
        time_steps = int(time_steps_var.get())
        
        u0 = initialCond(poly_str, nx, dx)
        u = heatEqn1D(u0, alpha, dx, dt, time_steps)
        animate_1d_heat_equation(u, dx, dt)
    
    def animate_1d_heat_equation(u, dx, dt):
        """Animates the 1D heat equation solution."""
        fig, ax = plt.subplots()
        line, = ax.plot(np.linspace(0, dx * (u.shape[1] - 1), u.shape[1]), u[0, :])
        ax.set_xlabel("Position")
        ax.set_ylabel("Temperature")
        ax.set_title("1D Heat Equation Simulation")
        
        def update(frame):
            line.set_ydata(u[frame, :])
            return line,
        
        ani = animation.FuncAnimation(fig, update, frames=u.shape[0], interval=50, blit=True)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        canvas.draw()
    
    def reset_values():
        poly_entry.delete(0, tk.END)
        poly_entry.insert(0, "x**2 - x")
        alpha_var.set(0.1)
        nx_var.set(50)
        dx_var.set(0.1)
        dt_var.set(0.01)
        time_steps_var.set(100)
    
    root = tk.Tk()
    root.title("1D Heat Equation Simulation")
    
    frame = ttk.Frame(root, padding=10)
    frame.pack()
    
    ttk.Label(frame, text="Initial Condition (Polynomial)").pack()
    poly_entry = ttk.Entry(frame, width=20)
    poly_entry.insert(0, "x**2 - x")
    poly_entry.pack()
    
    alpha_var = tk.DoubleVar(value=0.1)
    ttk.Label(frame, text="Alpha").pack()
    ttk.Scale(frame, from_=0.01, to=1.0, variable=alpha_var, orient='horizontal').pack()
    
    nx_var = tk.IntVar(value=50)
    ttk.Label(frame, text="Grid Points").pack()
    ttk.Scale(frame, from_=10, to=200, variable=nx_var, orient='horizontal').pack()
    
    dx_var = tk.DoubleVar(value=0.1)
    ttk.Label(frame, text="dx").pack()
    ttk.Scale(frame, from_=0.01, to=1.0, variable=dx_var, orient='horizontal').pack()
    
    dt_var = tk.DoubleVar(value=0.01)
    ttk.Label(frame, text="dt").pack()
    ttk.Scale(frame, from_=0.001, to=0.1, variable=dt_var, orient='horizontal').pack()
    
    time_steps_var = tk.IntVar(value=100)
    ttk.Label(frame, text="Time Steps").pack()
    ttk.Scale(frame, from_=10, to=1000, variable=time_steps_var, orient='horizontal').pack()
    
    button_frame = ttk.Frame(frame)
    button_frame.pack()
    
    ttk.Button(button_frame, text="Run Simulation", command=start_simulation).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="Reset", command=reset_values).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="Quit", command=root.quit).pack(side=tk.LEFT, padx=5)
    
    root.mainloop()
        
if __name__ == '__main__':
    runSim()