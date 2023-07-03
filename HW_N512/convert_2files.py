import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import glob
import imageio

from PIL import Image
from boututils.datafile import DataFile
from boutdata.collect import collect

# sys.path.insert(n, item) inserts the item at the nth position in the list 
# (0 at the beginning, 1 after the first element, etc ...)
sys.path.insert(0, '../../../codes/TurboGenPY/')

from tkespec import compute_tke_spectrum2d
from isoturb import generate_isotropic_turbulence_2d



SAVE_UVW = False
DTYPE    = 'float32'
DIR      = 0  # orientation plot (0=> x==horizontal; 1=> z==horizontal). In BOUT++ z is always periodic!
STIME    = 201 # starting time to save fields
FTIME    = 1001 # starting time to take as last image
ITIME    = 10  # skip between STIME, FTIME, ITIME
NDNS     = 100
N        = 512
L        = 50.176 
delx     = L/N
dely     = L/N

useLogSca = True
xLogLim    = [1.0e-2, 100]   # to do: to make nmore general
yLogLim    = [1.e-10, 10.]
xLinLim    = [0.0e0, 600]
yLinLim    = [0.0e0, 1.0]

ttime  = []
Energy = []


def cr(phi, i, j):
    return np.roll(phi, (-i, -j), axis=(0,1))

def convert(x):
    return x

    


def save_fields(totTime, U, V, P, filename="restart.npz"):

    # save restart file
    np.savez(filename, t=totTime, U=U, V=V, P=P)


# create folders fields and paths
path = "fields"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
else:
    cmd = "rm fields/*"
    os.system(cmd)


# run on data
nMax = []
nMin = []
phiMax = []
phiMin = []
vortMax = []
vortMin = []
for nrun in range(NDNS):
    newfolder = "HW_data/HW_" + str(nrun) + "/data/"
    file_path = newfolder + "BOUT.log.0"
    with open(file_path, 'r') as file:
        content = file.read()
        if "finished" in content:
            
            os.chdir(newfolder)
            print("reading " + newfolder)
            
            for t in range(STIME,FTIME,ITIME):

                Img_n    = collect("n",    yind=0, tind=t, xguards=False, info=False)
                Img_phi  = collect("phi",  yind=0, tind=t, xguards=False, info=False)
                Img_vort = collect("vort", yind=0, tind=t, xguards=False, info=False)

                Img_n    = Img_n[0,:,0,:]
                Img_phi  = Img_phi[0,:,0,:]
                Img_vort = Img_vort[0,:,0,:]

                save_fields(t, Img_n, Img_phi, Img_vort, "../../../fields/fields_run" + str(nrun) + "_time" + str(t).zfill(3) + ".npz")

                print("done for file time step", t)

            os.chdir("../../../")
