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
hf = load('EzSecondBandFreqs.out') # TM Modes
hfi = load('EzSecondBandFreqsI.out') # TM Modes
ef = load('HzSecondBandFreqs.out') # TE Modes
efi = load('HzSecondBandFreqsI.out') # TM Modes

#plt.axhline(0.7)
#plt.axhspan(0.7 - 0.3, 0.7 + 0.3, alpha = 0.3)

for i in range(len(ef)):
    x = np.ones(np.shape(hf[i][4:])) * hf[i][1]
    plt.errorbar(x, hf[i][4:], fmt='bo')

    x = np.ones(np.shape(ef[i][4:])) * ef[i][1]
    plt.errorbar(x, ef[i][4:], fmt='ro')

x = [0,0.5]
plt.plot(x,x, 'k--')

plt.show()


for i in range(len(ef)):
    x = np.ones(np.shape(hf[i][4:])) * hf[i][1]
    plt.errorbar(x, hf[i][4:]/(-2*hfi[i][4:]), fmt='bo')

    x = np.ones(np.shape(ef[i][4:])) * ef[i][1]
    plt.errorbar(x, ef[i][4:]/(-2*efi[i][4:]), fmt='ro')

plt.yscale('log')
plt.show()

