#matplotlib inline
import matplotlib.pyplot as plt
from random import *
from numpy import *
import sys
# model parameters
"""
x = numero de presas
y = numero de depredadores
a = Tasa natural de crecimiento de la presa en ausencia del depredador.
b = Efecto de la depredación sobre la presa.
c = Tasa natural de muerte del depredador en ausencia de la presa.
e = Eficiencia y tasa de propagación del depredador en presencia de la presa.

a = 0.7; b = 0.5; c = 0.3;  e = 0.2
dt = 0.001; max_time = 100
t = 0; x = 1.0; y = 0.5
"""
def funcionLotka_Volterra(x,y,a,b,c,e,t,dt,max_time):
    t_list = []; x_list = []; y_list = []

    # initialize lists
    t_list.append(t); x_list.append(x); y_list.append(y)
    
    while t < max_time:
        # calc new values for t, x, y
        t = t + dt
        x = x + (a*x - b*x*y)*dt
        y = y + (-c*y + e*x*y)*dt
    
        # store new values in lists
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
    
    # Plot the results    
    p = plt.plot(t_list, x_list, 'b', t_list, y_list, 'r', linewidth = 2)
    
    plt.show()

# parametros originales

a = 0.7; b = 0.5; c = 0.3;  e = 0.2
dt = 0.0001; max_time = 100

t = 0; x = 1.0; y = 0.5
funcionLotka_Volterra(x,y,a,b,c,e,t,dt, max_time)

# primera modificación.

a = 0.9; b = 0.5; c = 0.3;  e = 0.2
dt = 0.0001; max_time = 100

t = 0; x = 1.0; y = 0.5
funcionLotka_Volterra(x,y,a,b,c,e,t,dt, max_time)

#segunda modificación. 
a = 0.7; b = 0.8; c = 0.3;  e = 0.2
dt = 0.0001; max_time = 100

t = 0; x = 1.0; y = 0.5
funcionLotka_Volterra(x,y,a,b,c,e,t,dt, max_time)

#tercera modificación

a = 0.7; b = 0.5; c = 0.6;  e = 0.2
dt = 0.0001; max_time = 100

t = 0; x = 1.0; y = 0.5
funcionLotka_Volterra(x,y,a,b,c,e,t,dt, max_time)

#cuarta modificación
a = 0.7; b = 0.5; c = 0.3;  e = 0.6
dt = 0.0001; max_time = 100

t = 0; x = 1.0; y = 0.5
funcionLotka_Volterra(x,y,a,b,c,e,t,dt, max_time)

#quinta modificación
a = 0.5; b = 0.5; c = 0.5;  e = 0.5
dt = 0.0001; max_time = 100

t = 0; x = 1.0; y = 0.5
funcionLotka_Volterra(x,y,a,b,c,e,t,dt, max_time)