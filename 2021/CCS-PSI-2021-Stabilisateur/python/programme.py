import numpy as np
import matplotlib.pyplot as plt
import math as m

alpha_i = m.radians(-35)
alpha_f = m.radians(45)

l = 25
L = 52
yG = 5
zG = 200
m3 = 1.25
g=9.81

def calc_L(alpha):
    """
    Détermine la longueur de la diagonale du parallèlogramme en fonction d'un angle alpha. 
    Cela correspond à la longueur du ressort.
    """
    return np.sqrt(L*L+l*l-2*L*l*np.sin(alpha))
    
def calc_beta(alpha):
    """ 
    Détermine beta en fontion de alpha.
    """
    return np.arctan2(L*np.sin(alpha)-l,L*np.cos(alpha))
    
def calc_yz_sspert(alpha):
    # Calcul des coordonnées du point G
    Lr = calc_L(alpha)
    yA=0
    y = yA+yG+L*np.cos(alpha) 
    z = zG+L*np.sin(alpha) 
    return np.array([y,z])
    
def calc_Fr(alpha):
    beta = calc_beta(alpha)
    return -m3*g*np.cos(alpha)/(np.sin(alpha-beta))
    
def plot_Lr():
    # Affichage de la longueur du ressort
    les_alpha = np.linspace(alpha_i,alpha_f,1000)
    les_L = calc_L(les_alpha)
    plt.clf()
    plt.grid()
    plt.plot(np.degrees(les_alpha),les_L)
    plt.show()
    
def plot_yz():
    # Affichage de la trajectoire du point G
    les_alpha = np.linspace(alpha_i,alpha_f,1000)
    X,Y = calc_yz_sspert(les_alpha)
    plt.clf()
    plt.grid()
    plt.axis("equal")
    plt.plot(X,Y)
    plt.show()

    
def plot_beta():
    # Evolution de l'angle beta
    les_alpha = np.linspace(alpha_i,alpha_f,1000)
    les_beta = calc_beta(les_alpha)
    plt.clf()
    plt.grid()
    plt.plot(np.degrees(les_alpha),np.degrees(les_beta))
    plt.show()
    
def plot_Fr():
    # Evolution de Fr
    les_alpha = np.linspace(alpha_i,alpha_f,1000)
    Fr = calc_Fr(les_alpha)
    plt.clf()
    plt.grid()
    plt.plot(np.degrees(les_alpha),Fr)
    plt.show()
    
def dichotomie(f, a, b, epsilon):
    """Zéro de f sur [a,b] à epsilon près, par dichotomie
       Préconditions : f(a) * f(b) <= 0 f continue sur [a,b]
                       epsilon > 0"""
    c, d = a, b
    fc, fd = f(c), f(d)
    while d - c > 2 * epsilon:
        m = (c + d) / 2.
        fm = f(m)
        if fc * fm <= 0:
            d, fd = m, fm
        else:
            c, fc = m, fm
    return (c + d) / 2.

def TRS(alpha):
    beta = calc_beta(alpha)
    Fr = calc_Fr(alpha)
    return -m34*g*m.cos(alpha)-Fr*m.sin(alpha-beta)

def angle_equilibre(m4):
    global m34
    m34 = m3+m4
    return dichotomie(TRS,alpha_i,alpha_f,10**-10)
    
def plot_eq():
    les_m4 = np.linspace(0,2,1000)
    les_angle = [angle_equilibre(m4) for m4 in les_m4]
    plt.cla()
    plt.plot(les_m4,np.degrees(les_angle),".")
    
    plt.grid()
    plt.show()
    
#plot_eq()


## AN
Tm = 0.1
wco=3/Tm
dphi = m.radians(45)
T = m.tan(0.5*(dphi+m.pi/2))/wco
L=52
m34 = 2.8
N = 100
K = 2*T*m34/L*(wco**3)/(1+T*T+wco**2)
#plot_Lr()
#plot_yz()
#plot_beta()
#plot_Fr()