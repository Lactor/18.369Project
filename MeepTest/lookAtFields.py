import h5py
import numpy as np
import matplotlib.pyplot as plt

files = ['Results/YOUSHOULDNAMEYOURFILE-hx-000280.34.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000280.68.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000281.01.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000281.35.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000281.69.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000282.03.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000282.36.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000282.70.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000283.04.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000283.38.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000283.71.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000284.05.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000284.39.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000284.73.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000285.06.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000285.40.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000285.74.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000286.07.h5',
         'Results/YOUSHOULDNAMEYOURFILE-hx-000286.41.h5']

b = []
for i in files:
    print i
    b.append(h5py.File(i, 'r'))

for i in range(len(b)):
    fig, ax = plt.subplots()
    ax.imshow(np.transpose(b[i]['hx.r'][:,0,:]))
    plt.savefig(files[i] + '.png')

    
