import h5py 
import numpy as np
import matplotlib.pyplot as plt

eps = 0.00000001

def C(filenames, f, kx):
    F = {}
    F['x'] = h5py.File(filenames['x'], 'r')
    F['y'] = h5py.File(filenames['y'], 'r')
    
    x = np.arange(-0.5, 0.5+eps, 1.0/(np.shape(F['x'][f+'x.r'][:])[0]-1))
    z = np.ones((1, np.shape(F['x'][f+'x.r'][:])[1]))

    Z,X = np.meshgrid(z,x)

    X = X[:,60:-60]
    print np.shape(X)

    Fx = F['x'][f+'x.r'][:,60:-60] + 1j* F['x'][f+'x.i'][:,60:-60]
    Fy = F['y'][f+'y.r'][:,60:-60] + 1j* F['y'][f+'y.i'][:,60:-60]

    #Fx = F['x'][f+'x.r'][:] + 1j* F['x'][f+'x.i'][:]
    #Fy = F['y'][f+'y.r'][:] + 1j* F['y'][f+'y.i'][:]


    #Fx *= np.exp(-1j*kx*X)
    #Fy *= np.exp(-1j*kx*X)

    plt.imshow(np.transpose(np.real(Fx)))
    #print np.max(np.abs(Fx))
    #print np.min(np.abs(Fx))
    
    plt.show()

    cx = np.sum(Fx)
    cy = np.sum(Fy)

    print cx
    print cy
    print np.angle(cx)

    cx *= np.exp( -1j*np.angle(cx))
    cy *= np.exp( -1j*np.angle(cx))

    print cx
    print cy
    return (cx, cy)



filenames = {'x': 'Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02-ex-001300.60.h5',
             'y': 'Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02-ey-001300.60.h5'}
print "#####"
print C(filenames, 'e', 0.25)
print "#####"

filenames = {'x': 'Results/EzSingle_fcen0.655_df0.01-ex-001300.90.h5',
             'y': 'Results/EzSingle_fcen0.655_df0.01-ey-001300.90.h5'}

print C(filenames, 'e', 0.25)
    
filenames = {'x': 'Results/EzSingle_fcen0.655_df0.01-ex-001301.43.h5',
             'y': 'Results/EzSingle_fcen0.655_df0.01-ey-001301.43.h5'}

print C(filenames, 'e', 0.25)



print ""


filenames = {'x': 'Results/EzSingle_fcen0.655_df0.01-hx-001301.43.h5',
             'y': 'Results/EzSingle_fcen0.655_df0.01-hy-001301.43.h5'}
print C(filenames, 'h', 0.25)



