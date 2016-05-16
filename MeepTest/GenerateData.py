import os
import numpy as np
import glob
from ComputeC import *

fcen = 0.9
df = 0.2
sourcex = -0.2
sourcey = -0.1
Ez = 'false'
h = 1

def ntost(d):
    st = "%.3f"%(d)
    while st[-1] == '0':
        st = st[:-1]
    if st[-1] == '.':
        st += '0'
    return st

# Generate Q data
if True:
    k_interpx = 0
    k_interpy = 18
    kxmax = 0
    kxmin = 0
    kymin = 0
    kymax = 0.5

    filename = 'Q_fcen%.2f_df%.2f_h%.2f_Ez%s.out' % (fcen, df, h, Ez)

    command = 'meep fcen=%.2f df=%.2f sourcex=%.2f sourcez=%.2f h=%.2f Ez?=%s single-mode?=false k-interpx=%d k-interpy=%d kxmax=%.2f kxmin=%.2f kymin=%.2f kymax=%.2f  Mode.ctl > %s' % ( fcen, df, sourcex, sourcey, h, Ez, k_interpx, k_interpy, kxmax, kxmin, kymin, kymax, filename)
    
    print "RUNNING THE Q Code:"
    print command
    os.system(command)
    
    command = "grep freqs: %s | cut -d ' ' -f 2-  > %s_freqs.out"%(filename, filename[:-4])
    print command
    os.system(command)
    command = "grep freqs-im: %s | cut -d ' ' -f 2- > %s_freqsI.out"%(filename, filename[:-4])
    print command
    os.system(command)


if False:

    # Corners = [np.array([-0.025, 0.38]),
    #            np.array([0.025, 0.38]),
    #            np.array([0.025, 0.47]),
    #            np.array([-0.025, 0.47]),
    #            np.array([-0.025, 0.38]),
    #            np.array([-0.025, -0.38]),
    #            np.array([0.025, -0.38]),
    #            np.array([0.025, -0.47]),
    #            np.array([-0.025, -0.47]),
    #            np.array([-0.025, -0.38])]
    
    # Corners = [np.array([-0.055, -0.02]),
    #            np.array([-0.04, -0.02]),
    #            np.array([-0.04, 0.02]),
    #            np.array([-0.055, 0.02]),
    #            np.array([-0.055, -0.02]),
    #            np.array([0.055, -0.02]),
    #            np.array([0.04, -0.02]),
    #            np.array([0.04, 0.02]),
    #            np.array([0.055, 0.02]),
    #            np.array([0.055, -0.02])]


    #Corners = [#np.array([-0.085,0.03]),
               #np.array([-0.07, 0.03]),
               #np.array([-0.07, -0.03]),
               #np.array([-0.085, -0.03]),
               #np.array([-0.085,0.03]),
               #np.array([0.085,0.03]),
               #np.array([0.07, 0.03]),
               #np.array([0.07, -0.03]),
               #np.array([0.085, -0.03]),
               #np.array([0.085,0.03]),
               #np.array([-0.005, -0.06]),
               #np.array([0.005, -0.06]),
               #np.array([0.005, 0.06]),
               #np.array([-0.005, 0.06]),
               #np.array([-0.005, -0.06])]
    Corners = [np.array([-0.05, -0.05]),
               np.array([-0.05, 0.05]),
               np.array([0.05, 0.05]),
               np.array([0.05, -0.05]),
               np.array([-0.05, -0.05])]
              
    # Corners = [np.array([0.03, -0.025]),
    #            np.array([0.06, -0.025]),
    #            np.array([0.06, -0.012]),
    #            np.array([0.03, -0.012]),
    #            np.array([0.03, -0.025]),
    #            np.array([0.03, -0.00]),
    #            np.array([0.06, -0.00]),
    #            np.array([0.06, 0.012]),
    #            np.array([0.03, 0.012]),
    #            np.array([0.03, 0]),
    #            np.array([0.03, 0.025]),
    #            np.array([0.06, 0.025]),
    #            np.array([0.06, 0.025]),
    #            np.array([0.03, 0.025]),
    #            np.array([0.03, 0.25]),
    #            np.array([0.03, -0.038]),
    #            np.array([0.06, -0.038]),
    #            np.array([0.06,  0.038]),
    #            np.array([0.03,  0.038]),
    #            np.array([0.03, -0.38])]
    


    
    n = [5,5,5,5,9,2,-1,9,2,9,2,-1,9,1,9,1,-1,9,1,9,1,5,5,5,5,5,5,5]
    

    # Generate points in k space
    k = []
    
    for l in range(4):
        print l
        dc = (Corners[l+1]- Corners[l])/(n[l]-1) 
        for i in range(n[l]-1):
            k.append(Corners[l] + i*dc)
            
    # for l in range(5,9):
    #     dc = (Corners[l+1]- Corners[l])/(n[l]-1) 
    #     for i in range(n[l]-1):
    #         k.append(Corners[l] + i*dc)

    # for l in range(10,14):
    #     dc = (Corners[l+1]- Corners[l])/(n[l]-1) 
    #     for i in range(n[l]-1):
    #         k.append(Corners[l] + i*dc)
    # for l in range(15,19):
    #     dc = (Corners[l+1]- Corners[l])/(n[l]-1) 
    #     for i in range(n[l]-1):
    #         k.append(Corners[l] + i*dc)
    
    output_file = 'pol_fcen%.2f_df%.2f_h%.2f_Ez%s.out'%(fcen, df, h,Ez)
    print output_file
    output = open(output_file, 'w')
    
    for kpoint in k:
        filename = "kx_%.3fky_%.3f.out"%( kpoint[0], kpoint[1])
        command = "meep fcen=%.2f df=%.2f sourcex=%.2f sourcez=%.2f h=%.2f Ez?=%s single-mode?=true targetkx=%.3f targetky=%.3f Symmetry_Breaking.ctl > %s" % ( fcen, df, sourcex, sourcey, h,  Ez, kpoint[0], kpoint[1], filename)
        print "RUNNING:"
        print command
        print ""
        os.system(command)
        
        # f = ['ex','ey','ez','hx','hy','hz']
        # #os.system('cd Results')
        # Field = "E"
        # if not Ez:
        #     Field = "H"
             
        # res = 'Results/'
        # base='SYM%szSingle_fcen%s_df%s_kx%s_ky%s_h%s_res20'%(Field, str(fcen), str(df), str(kpoint[0]), str(kpoint[1]), str(h))
        # print base
        # for i in f:
        #     command = 'h5topng -RZc dkbluered -C %s.h5 %s.h5; convert %s.png %s.gif'%(res+base+'-eps-*', res+base+'-'+i+'-*', res+base+'-'+i+'-*', res+base+'-'+i)
        #     print command
        #     os.system(command)

        # #os.system('cd ..')

        command = "grep CX_E_TOP: %s | cut -d ' ' -f 2- | tr 'i' 'j' > tempx.out"%(filename)
        print command
        os.system(command)
        print command
        command = "grep CY_E_TOP: %s | cut -d ' ' -f 2- | tr 'i' 'j' > tempy.out"%(filename)
        os.system(command)
    
        #files = {'x': l[0], 'y': l[1]}
        #(tx,ty) = C(files, 'e', kpoint[0])
        tx = np.loadtxt('tempx.out', dtype=complex)
        ty = np.loadtxt('tempy.out', dtype=complex)
        print "TOP"
        print tx, ty

        command = "grep CX_E_BOT: %s | cut -d ' ' -f 2- | tr 'i' 'j' > tempx.out"%(filename)
        print command
        os.system(command)
        print command
        command = "grep CY_E_BOT: %s | cut -d ' ' -f 2- | tr 'i' 'j' > tempy.out"%(filename)
        os.system(command)
        
        base='%szSingle_fcen%s_df%s_kx%s_ky%s_h%s_res20'%('E', str(fcen), str(df), ntost(kpoint[0]), ntost(kpoint[1]), str(h))

        #files = {'x': l[0], 'y': l[1]}
        #(tx,ty) = C(files, 'e', kpoint[0])
        bx = np.loadtxt('tempx.out', dtype=complex)
        by = np.loadtxt('tempy.out', dtype=complex)
        print "BOT"
        print bx, by
        
        
        #print tx
        #print ty
    
        string = '%.3f %.3f %f%s%fj %f%s%fj %f%s%fj %f%s%fj'%(kpoint[0], kpoint[1], np.real(tx), (np.imag(tx)>=0)*"+", np.imag(tx), np.real(ty), (np.imag(ty)>=0)*"+",  np.imag(ty),np.real(bx), (np.imag(bx)>=0)*"+", np.imag(bx), np.real(by), (np.imag(by)>=0)*"+",  np.imag(by))
        #print string
        output.write(string + '\n')

    print ""
    print ""
    print "Polarizations in %s"%(output_file)
        
    output.close()




















































































































































