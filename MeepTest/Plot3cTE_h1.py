import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from mpl_toolkits.axes_grid1.inset_locator import inset_axes,mark_inset
from mpl_toolkits.axes_grid1 import make_axes_locatable

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

def drawEllipse(x0,y0, cx, cy, size, ax):

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

    ax.plot(x,y, "r-")


# 3c h1.4 DATA
#hf = load('Q_fcen0.80_df0.40_h1.40_Eztrue_freqs.out', True) # TM Modes
#hfi = load('Q_fcen0.80_df0.40_h1.40_Eztrue_freqsI.out', True) # TM Modes

hf_f = load('Q_fcen0.80_df0.20_h1.00_Ezfalse_freqs.out', True) # TM Modes
hfi_f= load('Q_fcen0.80_df0.20_h1.00_Ezfalse_freqsI.out', True) # TM Modes


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

fig, ax = plt.subplots()

pol = np.loadtxt('pol_fcen0.82_df0.10_h1.00_Ezfalse.out', delimiter =' ',  dtype=complex)


Qh_f = hf_f[:,4]/(-2 * hfi_f[:,4])
X_f = hf_f[:,1]
Y_f = hf_f[:,2]
Qh_f = np.rot90(np.resize(Qh_f, ( np.size(np.unique(X_f)), np.size(np.unique(Y_f)))))


Data = np.log10(np.abs(Qh_f))
a= ax.imshow(Data, extent=[np.min(X_f),np.max(X_f),np.min(Y_f),np.max(Y_f)], interpolation='none')
ax.set_xlim([np.min(X_f),np.max(X_f)])
ax.set_ylim([np.min(Y_f),np.max(Y_f)])

ax.set_ylabel('$k_y$')
ax.set_xlabel('$k_x$')

divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad =0.05)

plt.colorbar(a, cax = cax, label='$\log_{10}(Q)$')

#plt.colorbar( label='$\log_{10}(Q)$')

for i in range(len(pol[:,0])):
    drawEllipse(pol[i,0],pol[i,1], pol[i,2], pol[i,3], 0.005, ax)


#Data = Qh



# File containing the polarizations, kx, ky, cx, cy

#plt.xlim([-0.05, 0.05])
#plt.ylim([-0.5, 0.5])



#plt.xticks([-0.05, 0.05])
#plt.yticks([-0.3, 0 , 0.5])


plt.savefig('h1.eps')
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#ax.plot_wireframe(X,Y,E)

plt.show()



