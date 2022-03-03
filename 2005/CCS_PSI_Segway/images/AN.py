h=0.95
mH = 80
AH = 18
BH = 20
CH = 1.2

mS = 25
AS = 0.8
BS = 1.2
CS = 1.3

L = 0.65
R = 0.24
mR = 5
AR = 0.28

g = 9.81

A = mH*h*h + AH + AS
B = mH*h
C = mH*h *g
D = mH + mS+ 2*mR + 2*AR/R/R


alpha = -C/(B+D*R)


dv = 7*22*3.14/180
td = 20000/3600/dv
dd = td*20000/3600

# Temps pour passer de 0 à 20 km/h
a = 7
ta = 20000/3600/a # va = a*ta
print(ta)
da = 0.5*ta * 20000/3600
print(da)

import math as m
p12 = m.sqrt((C*D)/(D*A-B*B))
print(p12)

