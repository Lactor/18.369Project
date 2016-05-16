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

    ax.plot(x,y, "w-")


# 3c h1.4 DATA
#hf = load('Q_fcen0.80_df0.40_h1.40_Eztrue_freqs.out', True) # TM Modes
#hfi = load('Q_fcen0.80_df0.40_h1.40_Eztrue_freqsI.out', True) # TM Modes

hf_p = load('3c_h_pos_freq.out', True) # TM Modes
hfi_p= load('3c_h_pos_freqI.out', True) # TM Modes

hf_n = load('3c_h_neg_freq.out', True) # TM Modes
hfi_n= load('3c_h_neg_freqI.out', True) # TM Modes

hf_f = load('3c_h_full_freq.out', True) # TM Modes
hfi_f= load('3c_h_full_freqI.out', True) # TM Modes


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

pol = np.loadtxt('3c_h_pol.out', delimiter =' ',  dtype=complex)


Qh_f = hf_f[:,4]/(-2 * hfi_f[:,4])
X_f = hf_f[:,1]
Y_f = hf_f[:,2]
Qh_f = np.rot90(np.resize(Qh_f, ( np.size(np.unique(X_f)), np.size(np.unique(Y_f)))))


Data = np.log10(Qh_f)
print "##########"
print np.max(Data)
a= ax.imshow(Data, vmin=4, vmax=8, extent=[np.min(X_f),np.max(X_f),np.min(Y_f),np.max(Y_f)], interpolation='none')
ax.set_xlim([-0.05, 0.05])
ax.set_ylim([-0.5, 0.5])

ax.set_ylabel('$k_y$')
ax.set_xlabel('$k_x$')

ax.set_xticks([-0.05, 0.05])


divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='15%', pad =0.05)

plt.colorbar(a, cax = cax, label='$\log_{10}(Q)$')

#plt.colorbar( label='$\log_{10}(Q)$')

for i in range(len(pol[:,0])):
    drawEllipse(pol[i,0],pol[i,1], pol[i,2], pol[i,3], 0.005, ax)

ax_n = plt.axes( [0.25, 0.15, 0.1, 0.35])


Qh_n = hf_n[:,4]/(-2 * hfi_n[:,4])
X_n = hf_n[:,1]
Y_n = hf_n[:,2]
Qh_n = np.rot90(np.resize(Qh_n, ( np.size(np.unique(X_n)), np.size(np.unique(Y_n)))))

print np.shape(Qh_n)
print Qh_n

ax_n.set_yticks([-0.34, -0.42, -0.50])
ax_n.set_xticks([np.min(X_n),np.max(X_n)])


Data = np.log10(Qh_n)
ax_n.imshow(Data, vmin=4, vmax=8, extent=[np.min(X_n),np.max(X_n),np.min(Y_n),np.max(Y_n)], interpolation='none')
#ax.imshow(Data,  vmin=0, vmax=10, extent=[np.min(X_n),np.max(X_n),np.min(Y_n),np.max(Y_n)])

mark_inset(ax, ax_n, loc1=1, loc2=3, fc='none', ec='0')

print [np.min(X_n),np.max(X_n)]
print [np.min(Y_n),np.max(Y_n)]


ax_n.set_xlim([np.min(X_n),np.max(X_n)])
ax_n.set_ylim([np.min(Y_n),np.max(Y_n)])


for i in range(len(pol[:,0])):
    drawEllipse(pol[i,0],pol[i,1], pol[i,2], pol[i,3], 0.015, ax_n)

ax_p = plt.axes([0.25, 0.6, 0.1, 0.35])

Qh_p = hf_p[:,4]/(-2 * hfi_p[:,4])
X_p = hf_p[:,1]
Y_p = hf_p[:,2]
Qh_p = np.rot90(np.resize(Qh_p, ( np.size(np.unique(X_p)), np.size(np.unique(Y_p)))))


Data = np.log10(Qh_p)
ax_p.imshow(Data, vmin=4, vmax=8, extent=[np.min(X_p),np.max(X_p),np.min(Y_p),np.max(Y_p)] , interpolation='none')
for i in range(len(pol[:,0])):
    drawEllipse(pol[i,0],pol[i,1], pol[i,2], pol[i,3], 0.015, ax_p)
mark_inset(ax, ax_p, loc1=2, loc2=4, fc='none', ec='0')


ax_p.set_xlim([np.min(X_p),np.max(X_p)])
ax_p.set_ylim([np.min(Y_p),np.max(Y_p)])

ax_p.set_yticks([0.34, 0.42, 0.5])
ax_p.set_xticks([np.min(X_p),np.max(X_p)])

#Data = Qh

plt.tight_layout()

# File containing the polarizations, kx, ky, cx, cy

#plt.xlim([-0.05, 0.05])
#plt.ylim([-0.5, 0.5])



#plt.xticks([-0.05, 0.05])
#plt.yticks([-0.3, 0 , 0.5])


plt.savefig('h1.4.eps')
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#ax.plot_wireframe(X,Y,E)

plt.show()



