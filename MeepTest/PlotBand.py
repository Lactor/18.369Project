import numpy as np
import matplotlib.pyplot as plt

def load(name, onlyFirst=False):

    f = open(name, 'r')
    b = []
    for line in f:
        t = line.split(',')
        temp = []
        for i in t:
            temp.append(float(i))
        if onlyFirst:
            if len(t) < 5:
                temp.append(-1)
            temp = temp[:5]
            #print t
            #print len(t)
        b.append(temp)

    b = np.array(b)
    return b

def drawEllipse(x0,y0, cx, cy, size):

    Cx = cx
    Cy = cy

    angle = np.arange(0, 2*np.pi, 1.0/20)
    x = np.real(np.exp(1j*angle) * cx)
    y = np.real(np.exp(1j*angle) * cy)
    maxsize = np.sqrt(np.max( x**2 + y**2))
  
    x *= size/maxsize
    y *= size/maxsize
    
    x += x0
    y += y0

    #print x
    #print y

    plt.plot(x,y, "r-")


#fr = load('squareFR2.out')
#fi = load('squareFI2.out')

#frt20 = load('replicFT20.out')
#fit20 = load('replicFIT20.out')

#fr = load('replicF.out')
#fi = load('replicFI.out')

#frt20 = load('replickyT20F.out')
#hf = load('EzSecondBandFreqs.out') # TM Modes
#hfi = load('EzSecondBandFreqsI.out') # TM Modes
#ef = load('HzSecondBandFreqs.out') # TE Modes
#efi = load('HzSecondBandFreqsI.out') # TM Modes

#hf = load('EzBand_h1.4.out', True) # TM Modes
#hfi = load('EzBand_h1.4I.out', True) # TM Modes

#hf = load('EzBand_h1.43_fcen0.88.out', True) # TM Modes
#hfi = load('EzBand_h1.43_fcen0.88I.out', True) # TM Modes

hf = load('3c_freq.out', True) # TM Modes
hfi = load('3c_freqI.out', True) # TM Modes


#ef = load('HzBand.out', True) # TE Modes
#efi = load('HzBandI.out', True) # TM Modes

#plt.axhline(0.7)
#plt.axhspan(0.7 - 0.3, 0.7 + 0.3, alpha = 0.3)

# for i in range(len(ef)):
#     x = np.ones(np.shape(hf[i][4:])) * hf[i][1]
#     plt.errorbar(x, hf[i][4:], fmt='bo')

#     x = np.ones(np.shape(ef[i][4:])) * ef[i][1]
#     plt.errorbar(x, ef[i][4:], fmt='ro')

# x = [0,0.5]
# plt.plot(x,x, 'k--')

# plt.show()



# for i in range(len(ef)):
#     x = np.ones(np.shape(hf[i][4:])) * hf[i][1]
#     plt.errorbar(x, hf[i][4:]/(-2*hfi[i][4:]), fmt='bo')

#     x = np.ones(np.shape(ef[i][4:])) * ef[i][1]
#     plt.errorbar(x, ef[i][4:]/(-2*efi[i][4:]), fmt='ro')

# plt.yscale('log')
# plt.show()
#print hf
Qh = hf[:,4]/(-2 * hfi[:,4])
#print Qh
#Qe = ef[:,4]/(-2 * efi[:,4])
X = hf[:,1]
Y = hf[:,2]

Qh = np.rot90(np.resize(Qh, ( np.size(np.unique(X)), np.size(np.unique(Y)))))
print Qh

plt.imshow(np.log10(Qh), extent=[np.min(X),np.max(X),np.min(Y),np.max(Y)])
plt.colorbar()

# File containing the polarizations, kx, ky, cx, cy
pol = np.loadtxt('pol.out', delimiter =' ', skiprows=1, dtype=complex)
for i in range(len(pol[:,0])):
    drawEllipse(pol[i,0],pol[i,1], pol[i,2], pol[i,3], 0.001)

plt.xlim([0.03, 0.06])
plt.ylim([-0.03, 0.03])

plt.show()

