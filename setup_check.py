import numpy as np
import scipy
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)

from scipy.integrate import quad
area,_ = quad(np.sin,0,np.pi)
print("Integral of sin(x) from 0 to pi:",round (area,6))

plt.plot(x,np.sin(x))
plt.title("Setup check")
plt.savefig("setup_check.png")
print("Saved setup_check.png")


