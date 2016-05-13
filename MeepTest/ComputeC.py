import h5py 
import numpy as np
import matplotlib.pyplot as plt

eps = 0.00000001

def C(filenames, f, kx):
    F = {}
    F['x'] = h5py.File(filenames['x'], 'r')
    F['y'] = h5py.File(filenames['y'], 'r')
    
    x = np.arange(-0.5, 0.5, 1.0/(np.shape(F['x'][f+'x.r'][:])[0]-1))
    #z = np.ones((1, np.shape(F['x'][f+'x.r'][:])[1]))
    #Z,X = np.meshgrid(z,x)

    PlanePosition = 40
    #bL = 60
    #X = X[:-1,tL:bL]
    #print np.shape(X)

    L = F['x'][f+'x.r'][:]
    L[:, PlanePosition] = 20
    plt.imshow(np.transpose(L))
    plt.colorbar()

    plt.show()

    Fx = F['x'][f+'x.r'][:-1,PlanePosition] + 1j* F['x'][f+'x.i'][:-1,PlanePosition]
    Fy = F['y'][f+'y.r'][:-1,PlanePosition] + 1j* F['y'][f+'y.i'][:-1,PlanePosition]

    #Fx = F['x'][f+'x.r'][:] + 1j* F['x'][f+'x.i'][:]
    #Fy = F['y'][f+'y.r'][:] + 1j* F['y'][f+'y.i'][:]


    Fx *= np.exp(-1j*kx*x * 2*np.pi)
    Fy *= np.exp(-1j*kx*x * 2*np.pi)

    #print Fx
    
    #print np.max(np.abs(Fx))
    #print np.min(np.abs(Fx))
    

    cx = np.sum(Fx)
    cy = np.sum(Fy)

    #print cx
    #print cy
    #print np.angle(cx)

    cy *= np.exp( -1j*np.angle(cx))
    cx *= np.exp( -1j*np.angle(cx))

    #plt.imshow(np.transpose(np.real(Fx)))
    #plt.show()
    
    #plt.plot(np.concatenate( (np.real(Fx), np.real(Fx) ) , axis = 0 ), 'r')
    #plt.plot(np.concatenate( (np.imag(Fx), np.imag(Fx) ) , axis = 0 ), 'r--')

    #plt.plot(np.concatenate( (np.real(Fy), np.real(Fy) ) , axis = 0 ), 'b')
    #plt.plot(np.concatenate( (np.imag(Fy), np.imag(Fy) ) , axis = 0 ), 'b--')
    plt.plot([np.real(cx),np.real(cy)],[np.imag(cx), np.imag(cy)], 'bo')
    plt.axvline(0)
    plt.axhline(0)
    plt.show()

    #print cx
    #print cy
    return (cx, cy)



filenames = {'x': 'Results/EzSingle_fcen0.82_df0.03_kx0.044_ky0.02_res20-ex-000635.80.h5',
             'y': 'Results/EzSingle_fcen0.82_df0.03_kx0.044_ky0.02_res20-ey-000635.80.h5'}
print "#####"
print C(filenames, 'e', 0.044)
print "#####"

filenames = {'x': 'Results/EzSingle_fcen0.82_df0.03_kx0.044_ky0_res20-hx-000635.80.h5',
             'y': 'Results/EzSingle_fcen0.82_df0.03_kx0.044_ky0_res20-hy-000635.80.h5'}

print "#####"
print C(filenames, 'h', 0.044)
print "#####"


