# Re-import necessary libraries after reset
import numpy as np
import matplotlib.pyplot as plt

# Define the time vector
t = np.linspace(0, 5, 400)

# Define the components of the solution
x_t = np.exp(2*t)
y_t = -np.exp(2*t) + 3*np.exp(t)
z_t = -5*t*np.exp(2*t) - 9*np.exp(t) + 7*np.exp(2*t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='x(t)', color='blue')
plt.plot(t, y_t, label='y(t)', color='green')
plt.plot(t, z_t, label='z(t)', color='red')
plt.title("Solution Components $x(t)$, $y(t)$, $z(t)$ over $t \\in [0, 5]$")
plt.xlabel("Time $t$")
plt.ylabel("Function values")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
