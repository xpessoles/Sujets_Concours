from math import cos, sin, atan, pi,sqrt
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

Ix3=0.08
m3=18
g=9.81
L0=0.3-0.55


Aeq=Ix3+m3*L0**2

#Q18
Rm=2.28
Lm=0.49*1E-3
ki=0.89
r=1e-2
Aeq=2
beta=25*1e8
K=(beta-ki**2/(Lm*r*Aeq))*Lm
alpha=r*Aeq/(ki**2+r*Aeq*K)
T=(2*(alpha/Lm)**(-0.5)-Rm)/K

#Q19
K1=(ki**2+r*Aeq*K)/(ki*Aeq)


#Q28
Kp11=1000*9.93+2338
Kp22=5*12.9-2921
Kv11=2*0.7*sqrt(1000*9.93)
Kv22=2*0.7*sqrt(5*12.9)

print(Kp11,Kp22,Kv11,Kv22)