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

def drawEllipse(x0,y0, cx, cy, size, ax, color='w'):

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

    ax.plot(x,y, color+"-")


# 3c h1.4 DATA
#hf = load('Q_fcen0.80_df0.40_h1.40_Eztrue_freqs.out', True) # TM Modes
#hfi = load('Q_fcen0.80_df0.40_h1.40_Eztrue_freqsI.out', True) # TM Mode

fig, ax = plt.subplots( ncols=3, nrows=1)

filesf = ['Sigma_z_1.00_freq.out','Sigma_z_1.05_freq.out','Sigma_z_1.1_freq.out']
filesfI = ['Sigma_z_1.00_freqI.out','Sigma_z_1.05_freqI.out','Sigma_z_1.1_freqI.out']
filesp = ['Sigma_z_1.00_pol.out','Sigma_z_1.05_pol.out','Sigma_z_1.1_pol.out']

for q in range(3):
    print q
    hf = load(filesf[q], True) # TM Modes
    hfi = load(filesfI[q], True) # TM Modes

    Qh = hf[:,4]/(-2 * hfi[:,4])
    #print Qh
    #Qe = ef[:,4]/(-2 * efi[:,4])
    X = hf[:,1]
    Y = hf[:,2]

    ax[q].set_xticks([0.03, 0.06])

    Qh = np.rot90(np.resize(Qh, ( np.size(np.unique(X)), np.size(np.unique(Y)))))
    
    E = np.rot90(np.resize(hf[:,4], ( np.size(np.unique(X)), np.size(np.unique(Y)))))
    Y = np.rot90(np.resize(Y, ( np.size(np.unique(X)), np.size(np.unique(Y)))))
    X = np.rot90(np.resize(X, ( np.size(np.unique(X)), np.size(np.unique(Y)))))
    Data = np.log10(np.abs(Qh))
    #Data = Qh

    print np.min(Data)
    print np.max(Data)

    im = ax[q].imshow(Data, vmin = 4, vmax=7, extent=[np.min(X),np.max(X),np.min(Y),np.max(Y)], interpolation = 'none')

    # File containing the polarizations, kx, ky, cx, cy
    pol = np.loadtxt(filesp[q], delimiter =' ', dtype=complex)
    for i in range(len(pol[:,0])):
        drawEllipse(pol[i,0],pol[i,1], pol[i,2], pol[i,3], 0.002, ax[q])
        drawEllipse(pol[i,0],pol[i,1], pol[i,4], pol[i,5], 0.002, ax[q], 'k')

    ax[q].set_xlim([np.min(X),np.max(X)])
    ax[q].set_ylim([np.min(Y),np.max(Y)])
    
    if q ==0:
        ax[0].set_ylabel('$k_y$')
        ax[0].set_yticks([-0.04, -0.02, 0, 0.02, 0.04])
        #ax[0].yaxis.tick_right()
    else:
        ax[q].set_yticks([])
    ax[q].set_xlabel('$k_x$')

divider = make_axes_locatable(ax[2])
cbar_ax = fig.add_axes([0.15, 0.98, 0.7, 0.02])
#cax = divider.append_axes('right', size='5%', pad =0.05)
fig.colorbar( im, cax = cbar_ax, label='$\log_{10}(Q)$', orientation='horizontal')
#plt.tight_layout()
plt.savefig('Sigma_z.eps')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X,Y,E)

plt.show()



