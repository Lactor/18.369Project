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

    tL = 30
    bL = 60
    X = X[:-1,tL:bL]
    #print np.shape(X)

    Fx = F['x'][f+'x.r'][:-1,tL:bL] + 1j* F['x'][f+'x.i'][:-1,tL:bL]
    Fy = F['y'][f+'y.r'][:-1,tL:bL] + 1j* F['y'][f+'y.i'][:-1,tL:bL]

    #Fx = F['x'][f+'x.r'][:] + 1j* F['x'][f+'x.i'][:]
    #Fy = F['y'][f+'y.r'][:] + 1j* F['y'][f+'y.i'][:]


    Fx *= np.exp(-1j*kx*X * 2*np.pi)
    Fy *= np.exp(-1j*kx*X * 2*np.pi)

    
    #print np.max(np.abs(Fx))
    #print np.min(np.abs(Fx))
    

    cx = np.sum(Fx)
    cy = np.sum(Fy)

    #print cx
    #print cy
    #print np.angle(cx)

    cx *= np.exp( -1j*np.angle(cx))
    cy *= np.exp( -1j*np.angle(cx))

    #plt.imshow(np.transpose(np.real(Fx)))
    #plt.show()
    
    plt.plot(np.concatenate( (np.real(Fx[:,0]), np.real(Fx[:,0]) ) , axis = 0 ), 'r')
    plt.plot(np.concatenate( (np.imag(Fx[:,0]), np.imag(Fx[:,0]) ) , axis = 0 ), 'r--')

    plt.plot(np.concatenate( (np.real(Fy[:,0]), np.real(Fy[:,0]) ) , axis = 0 ), 'b')
    plt.plot(np.concatenate( (np.imag(Fy[:,0]), np.imag(Fy[:,0]) ) , axis = 0 ), 'b--')


    plt.plot(np.concatenate( (np.real(Fx[:,20]), np.real(Fx[:,20]) ) , axis = 0 ), 'r')
    plt.plot(np.concatenate( (np.imag(Fx[:,20]), np.imag(Fx[:,20]) ) , axis = 0 ), 'r--')

    plt.plot(np.concatenate( (np.real(Fy[:,20]), np.real(Fy[:,20]) ) , axis = 0 ), 'b')
    plt.plot(np.concatenate( (np.imag(Fy[:,20]), np.imag(Fy[:,20]) ) , axis = 0 ), 'b--')

    print "Dif: ", np.real(Fx[-1,0] - Fx[0,0])
    plt.show()

    #print cx
    #print cy
    return (cx, cy)



filenames = {'x': 'Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02_res20-ex-001303.00.h5',
             'y': 'Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02_res20-ey-001303.00.h5'}
print "#####"
print C(filenames, 'e', 0.25)
print "#####"

filenames = {'x': 'Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02_res20-hx-001303.00.h5',
             'y': 'Results/EzSingle_fcen0.655_df0.01_kx0.25_ky0.02_res20-hy-001303.00.h5'}

print "#####"
print C(filenames, 'h', 0.25)
print "#####"


