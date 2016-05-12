import numpy as np
import matplotlib.pyplot as plt

def load(name):

    f = open(name, 'r')
    b = []
    for line in f:
        t = line.split(',')
        temp = []
        for i in t:
            temp.append(float(i))
        b.append(temp)

    b = np.array(b)
    return b

#fr = load('squareFR2.out')
#fi = load('squareFI2.out')

#frt20 = load('replicFT20.out')
#fit20 = load('replicFIT20.out')

#fr = load('replicF.out')
#fi = load('replicFI.out')

#frt20 = load('replickyT20F.out')
er = load('freqsHz.out')
hr = load('freqsEz.out')



for i in range(len(er)):
    x = np.ones(np.shape(er[i][4:])) * er[i][1]
    plt.errorbar(x, er[i][4:], fmt='bo')

    x = np.ones(np.shape(hr[i][4:])) * hr[i][1]
    plt.errorbar(x, hr[i][4:], fmt='ro')

x = [0,0.5]
plt.plot(x,x, 'k--')

plt.show()

