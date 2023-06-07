from math import cos, sin, atan, pi
L3=0.55
l3=0.3
l0=0.2

alpha=atan(l0/(L3-l3))
L0=(L3-l3)*cos(atan(l0/(L3-l3)))+l0*sin(atan(l0/(L3-l3)))

print(alpha,alpha*180/pi,L0)