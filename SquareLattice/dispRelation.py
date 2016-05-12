import numpy as np
import matplotlib.pyplot as plt

bands = np.loadtxt('slab.out', delimiter = ',', skiprows = 1)
bandsZ20 = np.loadtxt('slabZ20.out', delimiter = ',', skiprows = 1)
bandsZ20epshi4 = np.loadtxt('slabZ20epshi4.out', delimiter = ',', skiprows = 1)

Crystal2d = np.loadtxt('2DPhotonic.out', delimiter = ',', skiprows = 1)

x = bands[:,1]

for i in range(5, len(bands[0,:])):
    plt.plot(x, bands[:, i], 'bo-')
for i in range(5, len(bandsZ20[0,:])):
    plt.plot(x, bandsZ20[:, i], 'ro-')
for i in range(5, len(bandsZ20epshi4[0,:])):
    plt.plot(x, bandsZ20epshi4[:, i], 'go-')
for i in range(5, len(Crystal2d[0,:])):
    plt.plot(x, Crystal2d[:, i], 'ko-')


k = np.arange(0, 0.51, 0.01)
plt.plot(k,k, 'k--')
plt.plot(k, np.sqrt(1.0/12.0) * k, 'k--')
plt.show()
