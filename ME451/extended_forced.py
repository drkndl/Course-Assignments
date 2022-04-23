#!/usr/bin/env python
import numpy as np 

# Input parameters
T1 = 79
T2 = 68
T3 = 62
Ta = 33 		    # Ambient temperature 
To = 140.33 		# Base temperature 

# Surface mean temperature
Tmf = (T1 + T2 + T3) / 3
Tm = (Tmf + Ta) / 2
print("Tmf: ", Tmf, "Tm: ", Tm)

rho_air = 19.6754 * 10**-6       # Ns/m^2
Cp = 1.005 * 10**3          # J/kgK
Kair = 28.35345 * 10**-3	# W/mK
v = 18.08617 * 10**-6 		# m^2/s

g = 9.81
L = 150 * 10**-3
D = 12.5 * 10**-3
V = 						# Velocity of air (m/s)

# Perimeter
P = np.pi * D 
print("P: ", P)

# Ac
Ac = np.pi * D**2 / 4
print("Ac: ", Ac)

# Reynold's number
Dh = (4 * A) / P 
print("Dh: ", Dh)
Re = (V * Dh) / v 
print("Reynold's number: ", Re)

# Nusselt number
if Re > 40 and Re < 4000:
	Nu = 0.618 * (Re)**0.466
elif Re > 4000 and Re < 4*10**4:
	Nu = 0.174 * (Re)**0.618
print("Nusselt: ", Nu)

#hth
hth = Nu * Kair / D 
print("hth: ", hth)

# m 
m = np.sqrt((hth * P)/(K * Ac))
print("m: ", m)

# Fin effectiveness
Epsilon = np.tanh(m * L) / np.sqrt((hth * Ac)/(K * P))
print("Epsilon: ", Epsilon)

# Fin efficiency
Eta = np.tanh(m * L) / (m * L)
print("Eta: ", Eta)

# Actual heat transfer rate 
q = np.sqrt(hth * P * K * Ac) * (To - Ta) * np.tanh(m * L)
print("q: ", q)
