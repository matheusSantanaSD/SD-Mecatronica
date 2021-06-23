import math
import matplotlib.pyplot as matplot
from control.matlab import *
import numpy as np
#Necessaria a instalaçao das bibliotecas para rodar o codigo

def x_dot(t,x,u):
    A = np.array([[-2.0,-0.9],[10.0,0.0]])
    B = np.array([[-1.0],[0.0]])
    xkp1 = A @ x + B @ u
    
    return xkp1

def rk4(tk,h,xk,uk):
    xk = xk.reshape([2,1])
    uk = uk.reshape([1,1])

    k1 = x_dot(tk,xk,uk)
    k2 = x_dot(tk+h/2.0,xk+h*k1/2.0,uk)
    k3 = x_dot(tk+h/2.0,xk+h*k2/2.0,uk)
    k4 = x_dot(tk+h,xk+h*k3,uk)
    xkp1 = xk + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)

    return xkp1.reshape([2,])

if __name__ == '__main__':
    # Função de transferencia
    G = tf([9],[1,2,9])
    Gss = tf2ss(G)

    Ts = 0.01
    h = 1e-4
    maxT = 10
    mult = Ts/h
    t = np.arange(0,maxT,h)
    tu = np.arange(0,maxT,Ts)

    x = np.zeros([2,len(t)])
    u = np.zeros([len(tu)])
    r = np.ones([len(t)-1])
    y = np.zeros([len(t)-1])

    kmax = len(t)-1

    #variaveis PID para controle
    Kp = 32
    Ki = 128
    Kd = 2

    ekm1 = 0
    ukm1 = 0
    p = 0
    
    for k in range(kmax):
        y[k] = Gss.C @ x[:,k]
        if (k%mult)==0:
            ek = r[k]-y[k]
            u[p] = Kp * ek + ukm1 + (Ki*Ts/2)*(ek + ekm1) + (2*Kd/Ts)*(ek - ekm1) - ukm1
            ekm1 = ek
            ukm1 = u[p]
            p += 1
        x[:,k+1] = rk4(t[k],h,x[:,k],u[p-1])
    
    matplot.figure('1')
    matplot.subplot(2,1,1)
    matplot.plot(t,x[0,:])
    matplot.grid()
    matplot.ylabel('x_1')
    matplot.subplot(2,1,2)
    matplot.plot(t,x[1,:])
    matplot.grid()
    matplot.ylabel('x_2')

    matplot.figure('2')
    matplot.plot(t[0:-1],y,label='y_1')
    matplot.plot(t[0:-1],r,label='r_1')
    matplot.grid()
    matplot.ylabel('y_1')

    matplot.figure('3')
    matplot.plot(tu[0:len(u)],u,label='u_1')
    matplot.grid()
    matplot.ylabel('u_1')
    matplot.show()