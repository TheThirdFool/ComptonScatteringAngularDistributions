#This is a program to look at the angular distributions of compton scattering.
import math 
import numpy as np
import matplotlib.pyplot as plt	


def Dist(GammaE):
	r_0 = 2.82 #* 1E-15
	E_rm = 511 #keV
	alpha = GammaE / E_rm
	Darray = []

	#Dist per solid angle =

	theta = 0
	while(theta < (3 * np.pi)):
		bot = 1 + alpha * (1 - math.cos(theta))
		dist = r_0**2.0 / (2.0 * bot**2.0)
		top = alpha**2.0 * (1 - math.cos(theta))**2.0
		bot_2 = 1 + alpha * (1 - math.cos(theta))
		dist_2 = dist * (1 + (math.cos(theta))**2.0 + (top / bot_2))
		Darray.append(dist_2 / 100)
		theta = theta + 0.01

	return Darray


def Draw():

	plt.rcParams['font.serif'] = "Times New Roman"
	plt.rcParams['font.family'] = "serif"

	all_energies = [0, 200, 662, 1173, 10000]
	#all_energies = [0, 1173]
	r = np.arange(0, (3 * np.pi), 0.01)
	ax = plt.subplot(111, projection='polar')

	for energy in all_energies:
		name = str(energy) + " keV"
		Distribution = Dist(energy)
		ax.plot(r, Distribution, label=name)


	# Place a legend to the right of this smaller subplot.
	plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

	#ax.plot(theta, r)
	ax.set_rmax(0.08)
	ax.set_rticks([0.02, 0.04, 0.06, 0.08])  # less radial ticks
	ax.set_rlabel_position(225)  # get radial labels away from plotted line
	ax.grid(True)
	ax.set_title("Angular distribution of Compton scatterings", va='bottom')
	plt.show()


Draw()
