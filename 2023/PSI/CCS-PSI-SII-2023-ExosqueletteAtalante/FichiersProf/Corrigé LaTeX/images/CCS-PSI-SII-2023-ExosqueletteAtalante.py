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

# Question 12
b4 =  - 2.6**2 +3.4 * 1.9
b3 = 1.6 * 19.2 - 7.7 * 2.6  -11.5 * 1.9
b2 = -2.6 * 5.2 +7.7 * 19.2 - 2.6 * 15.9 +3.4 * 17.1 +108.2 * 1.9 
b1 = -7.7 * 5.2 + 15.9 * 19.2 -11.5 * 17.1
b0 = - 15.9 * 5.2 +108.2 * 17.1 

b4 = b4/b0
b3 = b3/b0
b2 = b2/b0
b1 = b1/b0
print(b4,b3,b2,b1)

a0 = 3.4/b0
a1 = -11.5/b0
a2 = 108.2/b0
print("a0,a1,a2",a0,a1,a2)


# Question 15
Aeq = 0.08 + 18 * L_0 **2
print("Aeq :",Aeq)


# Question 17
Lm  = 0.49e-3
ke = 0.89
ki = 0.89
r = 1/100
Aeq = 2
Kcapt = 1
xx = (5*10000)**2

K = (Lm*xx)-(ke*ki/r/Aeq)
K = K/Kcapt
print(K)