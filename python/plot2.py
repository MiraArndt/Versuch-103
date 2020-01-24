import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = (np.genfromtxt('csvData/EinseitigEckig.csv',delimiter=',',unpack=True,usecols=0))*0.01
y = np.genfromtxt('csvData/EinseitigEckig.csv',delimiter=',',unpack=True,usecols=1)*0.001
z = np.genfromtxt('csvData/EinseitigEckig.csv',delimiter=',',unpack=True,usecols=2)*0.001
x1=x*100
xrund=["%.0f" % elem for elem in x1]

y1=y*1000
yrund=["%.2f" % elem for elem in y1]

z1=z*1000
zrund=["%.2f" % elem for elem in z1]



diff=z-y
diff1=z1-y1

diffrund=["%.2f" % elem for elem in diff1]


with open("csvData/tabelle2.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(xrund,yrund,zrund,diffrund))

b=ufloat(0.009995,0.000012)
h=ufloat(0.009960,0.000013)
m=ufloat(0.09295,0.00222)

#print(11.855/(2*m*(h*b**3)/12))
xneu=(0.5*x**2-x**3/3)

params,covariance_matrix = np.polyfit(xneu,diff,deg=1,cov=True)
x_plot= np.linspace(0,0.08,200)
uncertainties= np.sqrt(np.diag(covariance_matrix))




plt.plot(xneu,diff, 'x',label='Messwerte')
#plt.plot((x),diff, 'x',label='Differenz')
plt.plot(x_plot,params[0]*x_plot+params[1],label='Ausgleichsgerade')

#for name, value, uncertainty in zip('ab', params, uncertainties): 
 #   print(f'{name} = {value:.5f} ± {uncertainty:.5f}')


plt.xlabel(r'$(Lx^2-\frac{x^3}{3})\,/\,\si{\cubic\meter}$')
plt.ylabel(r'$D\,/\,\si{\meter}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
