import h5py
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

f = h5py.File('slab-epsilon.h5', "r")
de = f['epsilon.xx'][:,0,:]
de = np.ma.masked_where(de > 2, de)
print de
#print np.shape(f['epsilon.xx'][:])
#plt.imshow(f['epsilon.xx'][:,0,:])

resolution = 32.0

fx = h5py.File('slab-e.k01.b01.x.zodd.h5', 'r')
fy = h5py.File('slab-e.k01.b01.y.zodd.h5', 'r')
#fz = h5py.File('slab-e.k05.b08.z.zodd.h5', 'r')

K = fy['Bloch wavevector'][:]

fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(12,12))
xt = fx['x.r'][:,0,:] + 1j*fx['x.i'][:,0,:]
yt = fy['y.r'][:,0,:] + 1j*fy['y.i'][:,0,:]
Phase = np.ones(np.shape(yt), dtype = np.complex_)

print K

for i in range(len(Phase[:,0])):
    for o in range(len(Phase[0,:])):
        Phase[i,o] = np.exp(-1j*(i*K[0] + o*K[2])/resolution*2*np.pi)
        #print x[i,o]
        yt[i,o] *= Phase[i,o]
        xt[i,o] *= Phase[i,o]

xr = np.concatenate((np.real(xt),np.real(xt),np.real(xt)))
xi = np.concatenate((np.imag(xt),np.imag(xt),np.imag(xt)))
yr = np.concatenate((np.real(yt),np.real(yt),np.real(yt)))
yi = np.concatenate((np.imag(yt),np.imag(yt),np.imag(yt)))

de = np.concatenate((de,de,de))


ax[0][0].imshow( xr)
ax[1][0].imshow( xi)
ax[0][0].imshow(de, cmap='Greys', alpha = 0.8, interpolation='none')

ax[0][1].imshow( yr)
ax[1][1].imshow( yi)
ax[2][1].imshow(de)

cx = np.sum(xt)
cy = np.sum(yt)

print cx, cy



plt.show()




