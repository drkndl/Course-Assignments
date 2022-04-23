import numpy as np 

# Input parameters
T1 = 79
T2 = 68
T3 = 62
Ta = 33 		    # Ambient temperature 
To = 107 		    # Base temperature 

# Surface mean temperature
Tmf = (T1 + T2 + T3) / 3
Tm = (Tmf + Ta) / 2
print("Tmf: ", Tmf, "Tm: ", Tm)

mu = 19.6754 * 10**-6       # Ns/m^2
Cp = 1.005 * 10**3          # J/kgK
Kair = 28.35345 * 10**-3	# W/mK
v = 18.08617 * 10**-6 		# m^2/s

g = 9.81
L = 150 * 10**-3
D = 12.5 * 10**-3

# Prandtl number
Pr = mu * Cp / Kair
print("Prandtl number: ", Pr)

# Grashoff number
B = 1 / (Tm + 273)
DelTheta = Tmf - Ta
print("Beta = ", B, "DelTheta = ", DelTheta)
Gr = D**3 * B * g * DelTheta / v**2
print("Grashoff number: ", Gr)

# Nusselt number
print("Gr.Pr: ", Gr*Pr)
if Gr * Pr > 100 and Gr * Pr < 10**4:
	Nu = 0.85 * (Gr * Pr)**0.19
elif Gr * Pr > 10**4 and Gr * Pr < 10**7:
	Nu = 0.48 * (Gr * Pr)**0.25
elif Gr * Pr > 1**7 and Gr * Pr < 10**12:
	Nu = 0.13 * (Gr * Pr)**(1/3)
print("Nusselt: ", Nu)

#hth
hth = Nu * Kair / D 
print("hth: ", hth)

# Perimeter
P = np.pi * D 
print("P: ", P)

K = 111 		    # Brass
# K = 45  			# Stainless steel
# K = 327 			# Copper

# Ac
Ac = np.pi * D**2 / 4
print("Ac: ", Ac)

# m 
m = np.sqrt((hth * P)/(K * Ac))
print("m: ", m)

# Fin effectiveness
Epsilon = np.tanh(m * L) / np.sqrt((hth * Ac)/(K * P))
print("Epsilon: ", Epsilon)

# Fin efficiency
Eta = np.tanh(m * L) / (m * L)
print("Eta: ", Eta)

# Temperature distribution
# X = 45 * 10**-3
# X = 90 * 10**-3 
X = 0                # T_base
Tx = Ta + (To - Ta) * (np.cosh(m * (L - X))) / np.cosh(m * L)
print("Tx: ", Tx, "for X: ", X)

# Actual heat transfer rate 
q = np.sqrt(hth * P * K * Ac) * (To - Ta) * np.tanh(m * L)
print("q: ", q)
