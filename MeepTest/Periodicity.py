import matplotlib.pyplot as plt
import numpy as np
import h5py


#f = h5py.File('Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02-ex-001300.53.h5', 'r')
c = 'h'
fz = h5py.File('Results/HzSingle_fcen0.655_df0.01-'+c + 'z-001300.98.h5','r')
fy = h5py.File('Results/HzSingle_fcen0.655_df0.01-'+c + 'y-001300.98.h5','r')
fx = h5py.File('Results/HzSingle_fcen0.655_df0.01-'+c + 'x-001300.98.h5','r')

    

Fz = fz[c+'z.r'][:] + 1j * fz[c+'z.i'][:]
Fy = fy[c+'y.r'][:] + 1j * fy[c+'y.i'][:]
Fx = fx[c+'x.r'][:] + 1j * fx[c+'x.i'][:]

x = np.arange(-0.5, 0.5, 1.0/np.shape(Fz)[0])
z = np.arange(0,1, 1.0/np.shape(Fz)[1])

t = [50,60,70,80,90,100]

for i in t:
    T = Fz[:, i] * np.exp(-1j*0.25*x * 2*np.pi)
    T /= T[0]

    plt.plot(x, np.real(T),'r-')
    plt.plot(x, np.imag(T),'b-')

    print "z", T[0]
    print T[-1]
    print np.sum(T)

    T = Fy[:, i] * np.exp(-1j*0.25*x * 2*np.pi)
    T /= T[0]

    plt.plot(x, np.real(T),'r--')
    plt.plot(x, np.imag(T),'b--')

    print "y", T[0]
    print T[-1]
    print np.sum(T)
    print ""
    
plt.show()

