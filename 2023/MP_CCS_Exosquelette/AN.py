import math as m
a = 100
b = 150
h0 = 100
deltah = 50


def calc_l2(h,phi):
    l2 = (b*m.cos(phi)-a)**2 + (b*m.sin(phi)+h)**2
    return l2**(.5)

