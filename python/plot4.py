import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = (np.genfromtxt('csvData/DoppelseitigEckig.csv',delimiter=',',unpack=True,usecols=0))*0.01
y = np.genfromtxt('csvData/DoppelseitigEckig.csv',delimiter=',',unpack=True,usecols=1)*0.001
z = np.genfromtxt('csvData/DoppelseitigEckig.csv',delimiter=',',unpack=True,usecols=2)*0.001

d=ufloat(0.009980,0.000012)
b=ufloat(0.009995,0.000012)
h=ufloat(0.009960,0.000013)
m1=ufloat(0.0095,0.0004)
m2=ufloat(0.0089,0.0006)
print(28.168/(48*m1*((d/2)**4/4)*np.pi))
print(28.168/(48*m2*((d/2)**4/4)*np.pi))


x1=x*100
xrund=["%.1f" % elem for elem in x1]

y1=y*1000
yrund=["%.2f" % elem for elem in y1]

z1=z*1000
zrund=["%.2f" % elem for elem in z1]



diff=z-y
diff1=z1-y1

diffrund=["%.2f" % elem for elem in diff1]


with open("csvData/tabelle4.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(xrund,yrund,zrund,diffrund))


xneu1=(3*0.552**2*x[0:7]-4*x[0:7]**3)
xneu2=4*(x[7:14]**3)-12*0.552*(x[7:14]**2)+9*(0.552**2)*x[7:14]-(0.552**3)

params1,covariance_matrix1 = np.polyfit(xneu1,diff[0:7],deg=1,cov=True)
x_plot1= np.linspace(0.05,0.167,200)
uncertainties1= np.sqrt(np.diag(covariance_matrix1))

for name, value, uncertainty in zip('ab', params1, uncertainties1): 
    print(f'{name} = {value:.10f} ± {uncertainty:.10f}')



params2,covariance_matrix2 = np.polyfit(xneu2,diff[7:14],deg=1,cov=True)
x_plot2= np.linspace(0.05,0.167,200)
uncertainties2= np.sqrt(np.diag(covariance_matrix2))

for name, value, uncertainty in zip('ab', params2, uncertainties2): 
    print(f'{name} = {value:.10f} ± {uncertainty:.10f}')



plt.subplot(2,1,1)
#plt.plot((x[0:7]),diff[0:7], 'x',label='Differenz-links')
plt.plot((xneu1),diff[0:7], 'x',label='Messwerte')
plt.plot(x_plot1,params1[0]*x_plot1+params1[1],label='Ausgleichsgerade')
plt.title(r'$x<L/2$')
plt.xlabel(r'$(3L^2x-4x^3) \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\meter}$')
plt.legend(loc='best')
plt.tight_layout()

plt.subplot(2,1,2)
#plt.plot((x[7:14]),diff[7:14], 'x',label='Differenz-rechts')
plt.plot((xneu2),diff[7:14], 'x',label='Messwerte')
plt.plot(x_plot2,params2[0]*x_plot2+params2[1],label='Ausgleichsgerade')
plt.title(r'$x>L/2$')

plt.xlabel(r'$(4x^3-12Lx^2+9L^2x-L^3) \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\meter}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot4.pdf')
