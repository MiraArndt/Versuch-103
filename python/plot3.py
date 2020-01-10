import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit

x = (np.genfromtxt('csvData/DoppelseitigRund.csv',delimiter=',',unpack=True,usecols=0))*0.01
y = np.genfromtxt('csvData/DoppelseitigRund.csv',delimiter=',',unpack=True,usecols=1)*0.001
z = np.genfromtxt('csvData/DoppelseitigRund.csv',delimiter=',',unpack=True,usecols=2)*0.001

diff=z-y

diffneu1=(3*0.552**2*diff[0:7]-4*diff[0:7]**3)
diffneu2=4*(diff[7:14]**3)-12*0.552*(diff[7:14]**2)+9*(0.552**2)*diff[7:14]-(0.552**3)

params1,covariance_matrix1 = np.polyfit(x[0:7],diffneu1,deg=1,cov=True)
x_plot1= np.linspace(0,0.276,200)
uncertainties1= np.sqrt(np.diag(covariance_matrix1))


params2,covariance_matrix2 = np.polyfit(x[7:14],diffneu2,deg=1,cov=True)
x_plot2= np.linspace(0.276,0.552,200)
uncertainties2= np.sqrt(np.diag(covariance_matrix2))

plt.plot((x[0:7]),diff[0:7], 'x',label='Differenz-links')
plt.plot((x[0:7]),diffneu1, 'x',label='DiffAngepasst-links')
plt.plot(x_plot1,params1[0]*x_plot1+params1[1],label='Ausgleichsgerade-links')


plt.plot((x[7:14]),diff[7:14], 'x',label='Differenz-rechts')
plt.plot((x[7:14]),diffneu2, 'x',label='DiffAngepasst-rechts')
plt.plot(x_plot2,params2[0]*x_plot2+params2[1],label='Ausgleichsgerade-rechts')


plt.xlabel(r'$x \:/\: \si{\meter}$')
plt.ylabel(r'$D \:/\: \si{\meter}$')
plt.legend(loc='best')

plt.savefig('build/plot3.pdf')
