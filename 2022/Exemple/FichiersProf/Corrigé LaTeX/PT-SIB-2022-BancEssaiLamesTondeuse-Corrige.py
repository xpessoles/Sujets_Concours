
# Q3
Fv = 30000 #N
mu  = 0.15
Di = 32.2 #mm
De = 60 #mm

Cadh = 1/3*mu *Fv * (De**3-Di**3)/(De**2-Di**2)
print("Cadh ",Cadh/1000, " Nm")


e = 1.5  # mm
b = 4    # mm
de = 42  # mm
Rm = 300 # MPa = N/mm²

C_cis = 2*Rm*e*b*de
print("Ccis ",C_cis/1000, " Nm")
