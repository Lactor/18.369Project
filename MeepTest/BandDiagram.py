import matplotlib.pyplot as plt
import numpy as np

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


TM = load('bandDiagram.out', True)
TE = load('banddiagramTE.out', True)


kx = np.where(TM[:,2] == 0)[0]
plt.plot(TM[kx,1], TM[kx, 4],'bo')
ky = np.where(TM[:,1] == 0)[0]
plt.plot(-TM[ky,2], TM[ky,4], 'bo')

kx = np.where(TE[:,2] == 0)[0]
plt.plot(TE[kx,1], TE[kx, 4],'ro')
ky = np.where(TE[:,1] == 0)[0]
plt.plot(-TE[ky,2], TE[ky,4], 'ro')


x = np.linspace(-0.5, 0.5, 101)
print x
y = np.abs(x)

y2 = np.abs(x)*0 + 1
plt.plot(x,y, 'y')
plt.fill_between(x, y, y2, where=y2 >= y, facecolor='yellow', alpha = 0.3, interpolate=True)

plt.xlim([-0.5, 0.5])
plt.axvline(0,color='k')

plt.xticks([-0.5, 0, 0.5], [r'$0.5\quad k_y$', '0', r'$0.5\quad k_x$'])
plt.ylabel(r'$\omega a/2\pi c$')
plt.savefig('BandDiagram.eps')
plt.show()
