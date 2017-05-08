#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math
mi=0.003
w=1.
dt=0.01
g=9.8
x=[10]
v=[0.]
t=[0.]
e=[0.]
a=[0.]

for tt in range(100000):
  x.append((x[-1]+v[-1]*dt+0.5*a[-1]*dt**2))
  t.append(t[-1]+dt)
  a.append(-np.sign(v[-1])*mi*g-w*x[-1])
  v.append(v[-1]+0.5*(a[-1]+a[-2])*dt)
  e.append(v[-1]**2/2.+w*x[-1]**2/2.)
  if x[-1] == 0:
   print t
  



plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,50,-20,20])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)

plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo} (s)')
plt.ylabel(r'\textit{$x(t)$}')

plt.yticks(np.linspace(-10,10,5,endpoint=True),
	[r'$- A$',r'$- \frac{A}{2}$','',r'$\frac{A}{2}$',r'$A$'])

plt.xticks(np.linspace(2*math.pi,12*math.pi,2*math.pi,endpoint=True),
	[r'$2\pi $',r'$4\pi$',r'$6\pi$',r'$8\pi$',r'$10\pi$',r'$12\pi$'])

plt.title(r'Oscilador Harm\^{o}nico com atrito- verlet', fontsize=18)

plt.axhline(y=10)
plt.axhline(y=-10)

plt.axvline(x=6*math.pi)
plt.axvline(x=4*math.pi)
plt.axvline(x=2*math.pi)
plt.plot(t,x,linewidth=1.5, label=r'\textit{$\mu = 0.003$}' )  
plt.legend(loc=0, mode='expand', ncol=0,prop={'size':6})
plt.savefig("verletx.pdf",dpi=96)

