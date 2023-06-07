from math import cos, sin, atan, pi
from numpy import array
L3=0.55
l3=0.3
l0=0.2

alpha=atan(l0/(L3-l3))
L0=(L3-l3)*cos(atan(l0/(L3-l3)))+l0*sin(atan(l0/(L3-l3)))

print(alpha,alpha*180/pi,L0)

#Q12 : calcul des coefficient de la fonction de transfert

D=array([-5.2*15.9+17.1*108.2,19.2*15.9-5.2*7.7-17.1*11.5,-2.6*15.9-5.2*2.6+19.2*7.7+1.9*108.2+17.1*3.4,-2.6*7.7+19.2*2.6-1.9*11.5,-2.6**2+1.9*3.4])

C=array([108.2,-11.5,3.4])

A=C/D[0]
B=D/D[0]

print(A)

print(B)