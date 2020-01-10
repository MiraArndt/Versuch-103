import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = (np.genfromtxt('csvData/EinseitigRund.csv',delimiter=',',unpack=True,usecols=0))*0.01
y = np.genfromtxt('csvData/EinseitigRund.csv',delimiter=',',unpack=True,usecols=1)*0.001
z = np.genfromtxt('csvData/EinseitigRund.csv',delimiter=',',unpack=True,usecols=2)*0.001

diff=z-y

diffneu=(3*0.5**2*diff-4*diff**3)

params,covariance_matrix = np.polyfit(x,diffneu,deg=1,cov=True)
x_plot= np.linspace(0,0.5,200)
uncertainties= np.sqrt(np.diag(covariance_matrix))


plt.plot((x),diffneu, 'x',label='DifferenzAngepasst')
plt.plot((x),diff, 'x',label='Differenz')
plt.plot(x_plot,params[0]*x_plot+params[1],label='Ausgleichsgerade')

plt.xlabel(r'$t \:/\: \si{\micro\second}$')
plt.ylabel(r'$\ln(U_{C,0})$')
plt.legend(loc='best')

plt.savefig('build/plot1.pdf')
