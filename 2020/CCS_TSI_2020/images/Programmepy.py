# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:39:26 2021

@author: xpess
"""

import numpy as np
import matplotlib.pyplot as plt
# Paramètres géométriques (mm)
a, b, c = 150, 400, 850
# Paramètres de la simulation (deg)
theta10min = -90 ; theta10max = 0 ; dtheta10 = 1
theta20min = 180 ; theta20max = 270 ; dtheta20 = 1
# Valeurs de tracé (deg)
theta10trace = -90, -60, -30, 0
theta20trace = 180, 210, 240, 270
def MGD(theta10, theta20):
    """
    Calcul des coordonnées de E connaissant theta10 et theta20 (en radians).
    Un des deux paramètres peut être un vecteur, les résultats sont alors des
    vecteurs de même taille que le vecteur passé en paramètre.
    """
    xB = a + b * np.cos(theta10)
    yB = b * np.sin(theta10)
    xD = -a + b * np.cos(theta20)
    yD = b * np.sin(theta20)
    alpha = np.arctan2(yB - yD, xB - xD)
    DM = np.sqrt((xB - xD)**2 + (yB - yD)**2) / 2
    ME = np.sqrt(c**2 - DM**2)
    xE = xD + DM * np.cos(alpha) + ME * np.sin(alpha)
    yE = yD + DM * np.sin(alpha) - ME * np.cos(alpha)
    return xE, yE

# Présentation du graphique
fig, (axTheta10, axTheta20) = plt.subplots(2, 1, sharex=True)
axTheta10.set_title("paramètre $\\theta_{10}$")
axTheta10.set_ylabel("$d x_E$ (mm)")
axTheta10.grid(True)
axTheta20.set_title("paramètre $\\theta_{20}$")
axTheta20.set_xlabel("$x_E$ (mm)")
axTheta20.set_ylabel("$d x_E$ (mm)")
axTheta20.grid(True)
theta20simu = np.radians(np.arange(theta20min - dtheta20, theta20max + 2*dtheta20, dtheta20))
for theta10 in theta10trace:
    xEinf, yEinf = MGD(np.radians(theta10 - dtheta10), theta20simu)
    xEmid, yEmid = MGD(np.radians(theta10), theta20simu)
    xEsup, yEsup = MGD(np.radians(theta10 + dtheta10), theta20simu)
    ####
    
    dxEsurDtheta10=(xEsup-xEinf)/(2*np.radians(dtheta10))
    dxEsurDtheta20=(xEmid[2 :]-xEmid[0 :-2])/(2* np.radians(dtheta20))
    dxE= dxEsurDtheta10[1 :-1] * np.radians(dtheta10)+ dxEsurDtheta20* np.radians(dtheta20)
    
     
    #### Fin de zone ####
    axTheta10.plot(xEmid[1:-1], dxE,label="$\\theta_{10}=$"+str(theta10))
    axTheta10.legend()
    
### PAS SUR DU TOUT
# Ajout des tracés à  theta20 constant
theta10simu = np.radians(np.arange(theta10min - dtheta10, theta10max + 2*dtheta10, dtheta10))
for theta20 in theta20trace:
    xEinf, yEinf = MGD(theta10simu,np.radians(theta20 - dtheta20))
    xEmid, yEmid = MGD(theta10simu,np.radians(theta20))
    xEsup, yEsup = MGD(theta10simu,np.radians(theta20 + dtheta20))
    
    #### Zone a completer
    dxEsurDtheta10=(xEsup-xEinf)/(2*np.radians(dtheta10))
    dxEsurDtheta20=(xEmid[2 :]-xEmid[0 :-2])/(2* np.radians(dtheta20))
    dxE= dxEsurDtheta10[1 :-1] * np.radians(dtheta10)+ dxEsurDtheta20* np.radians(dtheta20)
    #### Fin de zone ####
    
    axTheta20.plot(xEmid[1:-1], dxE,label="$\\theta_{20}=$"+str(theta20))

plt.legend()
plt.show()