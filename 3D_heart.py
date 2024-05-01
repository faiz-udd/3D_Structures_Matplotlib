import matplotlib.pyplot as plt
import numpy as np
#The Mathematical Equation for the heart shape belongs to Hamid Naderi, an Iraninan Mathematician
def x(t):
  return -1.5*(np.sin(2*t))**3 + 0.3*(np.sin(2*t))**7 + 0.1*np.sin(400*t)*(np.sin(2*t))**2 * (np.cos(6*t/5))**4

def y(t):
  return np.sin((8/3)*t + np.pi/6) + 0.25*(np.sin((8/3)*t + np.pi/6))**3 + 0.1*np.cos(400*t)*np.sin(2*t) * (np.cos(6*t/5))**4

def z(t):  # Add a z-component for the spiral effect
  return t  # Adjust the equation for desired spiral behavior

t = np.linspace(0, np.pi, 1000)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Calculate x, y, and z coordinates
X = x(t)
Y = y(t)
Z = z(t)

# Color based on z-axis value (adjust colormap as desired)
colors = plt.cm.viridis(Z / np.max(Z))  # Use viridis colormap

# Plot the 3D line with color
ax.plot_trisurf(X, Y, Z, cmap=plt.cm.viridis, linewidth=0.1, edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Heart-Shaped Spiral')

plt.show()
