import numpy as np
import matplotlib.pyplot as plt

# Parameters (adjust as needed)
L = 10  # Length of pipe
Th_in = 100  # Hot fluid inlet temperature
Tc_in = 50  # Cold fluid inlet temperature
N = 100  # Number of segments

# Discretize the pipe
dx = L / N
x = np.linspace(0, L, N+1)

# Initialize temperature arrays
Th = np.zeros(N+1)
Tc = np.zeros(N+1)
Th[0] = Th_in
Tc[0] = Tc_in

# Simplified heat transfer coefficient (adjust as needed)
U = 0.1

# Solve for temperature distribution (simplified example)
for i in range(N):
    Th[i+1] = Th[i] - U * dx * (Th[i] - Tc[i])
    Tc[i+1] = Tc[i] + U * dx * (Th[i] - Tc[i])

# Plot the results
plt.plot(x, Th, label='Hot Fluid')
plt.plot(x, Tc, label='Cold Fluid')
plt.xlabel('Length of Pipe')
plt.ylabel('Temperature')
plt.title('Temperature Variation Along Pipe')
plt.legend()
plt.grid(True)
plt.show()