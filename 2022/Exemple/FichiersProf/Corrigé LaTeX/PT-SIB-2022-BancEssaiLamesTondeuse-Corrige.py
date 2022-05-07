
# Q3
Fv = 30000 #N
mu  = 0.15
Di = 32.5 #mm
De = 60 #mm

Cadh = 1/3*mu *Fv * (De**3-Di**3)/(De**2-Di**2)
print("Cadh ",Cadh/1000, " Nm")
e = 1.5
b = 5