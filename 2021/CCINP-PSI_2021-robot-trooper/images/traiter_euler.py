import numpy as np
import matplotlib.pyplot as plt

def euler(F, a, b, y0, h):
    """Solution de y'=F(y,t) sur [a,b], y(a) = y0, pas h"""
    y = y0
    t = a
    y_list = [y0] # la liste des valeurs renvoyées
    t_list = [a] # la liste des temps
    while t+h <= b:
        y = y + h * F(y, t)
        y_list.append(y)
        t = t + h
        t_list.append(t)
    return t_list, y_list


####Definition des constantes
tf=11
Jm=3.4*1e-3
km=0.2
kt=km
Rm=1
A=Rm*Jm/(2*km*kt)
B=km/kt

def um(t):
    if t<1:
        return 4*t
    elif t<9:
        return 4
    elif t<10:
        return -4*(t-10)
    else:
        return 0

def F(y,t) :
    return (um(t)-B*y)/A


h=0.001
t_list,y_list = euler(F,0.0,tf,np.array([0.0,0.0]),h)
vt=[y[1] for y in y_list]


#Integration numerique
def T(f,t,y0):
    """Approximation de l'intégrale de a àb de f
    Méthode des trapèzes, N trapèzes"""
    S = y0
    L=[y0]
    h = (t[-1]-t[0])/len(t)
    for k in range(1,len(t)) :
        S = S + (f[k]+f[k-1])*0.5*h
        L.append(S)
    return L


t_list=np.linspace(0,11,11001)
ye=[um(k) for k in t_list]



h=0.001
t_list,y_list = euler(F,0.0,tf,np.array([0.0,0.0]),h)
vt=[y[1] for y in y_list]
position=T(vt,t_list,0)
y1=[y_list[k][0]for k in range(len(y_list))]
plt.figure(1, figsize=(7, 6))
ax=plt.subplot(2,1,1)
grid_x_ticks_minor = np.arange(0, 12, 1 )
ax.set_xticks(grid_x_ticks_minor)
plt.plot(t_list,vt,linestyle='--',label="v(t) simulée en (m/s)")
plt.plot(t_list,ye,linestyle='-',label="$u_m(t)$ en V (image de la vitesse de consigne)")
plt.legend(loc=8)
plt.xlabel('temps (en s)')
plt.ylabel('')
ax.grid()
ax2=plt.subplot(2,1,2)
plt.plot(t_list,position)
plt.xlabel('temps (en s)')
plt.ylabel('Position du robot simulée en m')
ax2.set_xticks(grid_x_ticks_minor)
ax2.grid()

plt.savefig('figure5.png')

