import numpy as np 
import matplotlib.pyplot as plt 

m = float(input("Enter the mass of the system in kg: "))
k = float(input("Enter the spring stiffness in N/m: "))
z = float(input("Enter the damping factor (zeta): "))
f = float(input("Choose whether the vibration is free (type '1') or forced (type '2'): "))

if f==2:
	w = float(input("Enter the harmonic frequency for the forced vibration in rad/s: "))

def free(m, k, z):
	wn = np.sqrt(k/m)
	fn = wn/2*np.pi
	T = 1/fn
	cc = 2*m*wn
	c = z*cc
	wd = wn*np.sqrt(1-z**2)
	q = 1/(2*z)

	return wn, fn, T, cc, c, wd, q

def forced(m, k, z, w):
	wn, fn, T, cc, c, wd, q = free(m, k, z)
	tr = np.sqrt((1 + (2*z*w/wn)**2)/((1 - (w/wn)**2)**2 + (2*z*w/wn)**2))
	phi = np.arctan((2*z*w/wn)/(1-(w/wn)**2))

	return tr, phi


wn, fn, T, cc, c, wd, q = free(m, k, z)
print("Angular natural frequency: %.3f rad/s" % (wn))
print("Natural frequency: %.3f Hz" % (fn))
print("Time period: %.3f s" % (T))
print("Critical damping factor: %.3f Ns/m" % (cc))
print("Damping factor: %2.3f Ns/m" % (c))
print("Damped natural frequency: %2.3f rad/s" % (wd))
print("Quality factor: %2.3f" % (q))

if int(f) == 2:
	tr, phi = forced(m, k, z, w)
	print("Transimissibility ratio: %.3f"% (tr))
	print("Phase angle: %.3f" % (phi))

	xarr = np.arange(0,4,0.01)
	z = [0.1, 0.3, 0.4, 0.5, 0.6, 1.0, 0.8, 2, 3]

	for zeta in z:

		yarr = np.sqrt(1/((1 - xarr**2)**2 + (2*zeta*xarr)**2))
		plt.plot(xarr, yarr, label=zeta)

	plt.title("Transmissibility vs Frequency Ratio for zeta from 0.3 to 5")
	plt.legend()
	plt.show()

