import math as m

l_0 = 0.2   #m
L_3 = 0.55  #m
l_3 = 0.3   #m

## Question 6
L_0 = l_0**2+(L_3-l_3)**2
L_0 = m.sqrt(L_0)
print("L0 ",L_0)

alpha = m.asin(l_0/L_0)
print("alpha :",alpha,"rad = ",m.degrees(alpha),'deg')

