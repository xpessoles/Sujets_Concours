tau1 = 1
K = 0.01
import math as m
K11 = (3.8**2+3.8*m.sqrt(3.8**2-4))/(2*K)

K12 = (3.8**2-3.8*m.sqrt(3.8**2-4))/(2*K)

KBO1 = K/(K*K11-1)

KBO2 = K/(K*K12-1)

om01 = m.sqrt(K*K11-1)/tau1
om02 = m.sqrt(K*K12-1)/tau1