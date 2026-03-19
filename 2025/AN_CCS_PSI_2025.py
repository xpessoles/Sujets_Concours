import numpy as np

alpha = np.radians(0.84)
Cx0 = 0.066
Cx  = 0.26
Cz0 = 0.4
Cz = 11.6
Cp0 = -0.045
Cp = 1.08
S = 8
m = 630
g = 9.81

cotalpha  = 1/(np.tan(alpha))

V = cotalpha*m*g
V = V/(S*0.5*(Cx0+Cx*alpha+cotalpha*(Cz0+Cz*alpha+Cp0+Cp*alpha)))
V = V**(.5)
print(V*3600/1000)