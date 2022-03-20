import numpy as np
import matplotlib.pyplot as plt
import math as m

d1 = 76
d4 = 70
h1 = 292

mE = 60
g = 9.8
D = 25/1000 # m
d = 10/1000 # m


 
les_beta = np.linspace(-45,30,100000)
les_lambda = np.sqrt(np.power(d1-d4*np.cos(np.radians(les_beta)),2)+np.power(h1-d4*np.sin(np.radians(les_beta)),2))

plt.plot(les_beta,les_lambda)
plt.xlabel("$\\beta$ (deg)")
plt.ylabel("$\\lambda$ (mm)")
plt.grid()
plt.show()

DeltaPMax = 16.8*mE*g/(m.pi*(D*D-d*d))
print(DeltaPMax*10e-6)