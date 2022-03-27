# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:58:31 2022

@author: xpess
"""

import math as m
# Q21 - Correcteur proportionnel
tau = (m.tan(m.radians((55+90)/2)))/0.13
print(tau)

def G(omega):
    res = 0.028/omega/omega
    res = res * 1/(m.sqrt(1+omega*omega/0.87/0.87))
    res = res/(m.sqrt(1+omega*omega*1.5*1.5))
    res = res * (1+tau*tau*omega*omega)/omega
    return res

print(G(0.13),1/G(0.13))


# Q23
# Module de r
om = 0.002
r = 0.0073*(1+24.4*24.4*om*om)/om
# module t
t = 1/r

print('module de t',(t*0.27*30*10e-6))

# Q26
omega_r = 35.7*3/4*10000 # °/s
print(omega_r)
omega_r = omega_r/360*60
print(omega_r)

# Q29
omr = 4e-4/35.7*2800
print(omr)
print(omr*360/60)

Cm = 1.3 * 0.01*(34* 1.26 + 0.65 * 0.6 (85 * 152 * 9.81* m.sin(2)/553)
print(Cm)