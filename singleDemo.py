"""
Simulation of a single compartment (in this case an artery)
"""


from __future__ import print_function
import os
from compartments import Artery
import matplotlib.pyplot as plt

tMax = 1.0       # integration end time
dt = 0.01                # time step size
t = 0


# generate a line of connected compartments
compartment = Artery(
    P1=9000.,
    P2=13000.,
    Q1=0.0003,
    Q2=0.0003
)

t_vals = []
P_vals = []
Q_vals = []
# integration and output
while t < tMax:
    t += dt
    P1, Q2 = compartment.integrate(t)
    t_vals.append(t)
    P_vals.append(P1)
    Q_vals.append(Q2)

print(P_vals)
f, ax = plt.subplots(2, sharex=True)
ax[0].set_title('Druck P')
ax[0].plot(t_vals, P_vals)
ax[1].set_title('Flussrate Q')
ax[1].plot(t_vals, Q_vals)
ax[1].set_xlabel("t")
plt.show()
