#DS3001 assignemnt q 

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y = np.log(x)
z= np.exp(x)
plt.scatter(x,y, label='Natural Log')
plt.scatter(x,z, label='Exponential')





plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc = 'lower right')
plt.title("Natural Log and Exponential Functions")
plt.show()


x = np.linspace(-6.5, 6.5, 100)
y =  np.sin(x)
z = np.cos(x)
plt.scatter(x,y, label='sine')
plt.scatter(x,z, label='cosine')


plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc = 'lower left')
plt.title("Sine and Cosine Functions")
plt.show()



def average(x):
    d= np.sum(x)
    f= len(x)
    return d/f

#result= average(x)

print('Mean:', average(x),'\n')


def standardD(number):
    n= len(x)
    mean= average(x)
    sumdiff= np.sum( (n-mean)**2)
    return sumdiff

print('Standard Deviation:', standardD(x),'\n')


def zscore(sample):
     zdiff = (x-average(x))/standardD(x)
     return (zdiff)

print('Z score', zscore(x)[1:10],'\n')


def variance(x,y):
    N = len(x)
    sumsqdiff = np.sum( (x-average(x))*(y-average(y)) )
    c = sumsqdiff / (N-1)
    return(c)
print('Covariance:', variance(x,y),'\n')



def correlation(x, y):
    c = variance(x, y)
    corx = standardD(x)
    cory = standardD(y)
    results = c / (corx * cory)
    return (results)

print('Correlation:', correlation(x, y), '\n')
