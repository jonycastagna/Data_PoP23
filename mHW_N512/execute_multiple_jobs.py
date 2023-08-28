import os
import numpy as np

NDNS = 100


np.random.seed(0)

for n in range(0,NDNS):
  r1 = np.random.random()       # seed mixmode x
  r2 = np.random.random()       # seed mixmode z

  cont = n%4

  if (cont==0):
    r3 = 1.0 #10**np.random.uniform(-1,0)   # alpha
    r4 = 1.0                          # kappa 
  if (cont==1):
    r3 = 1.0 #10**np.random.uniform(-1,0)   # alpha
    r4 = 1.0                            # kappa 
  if (cont==2):
    r3 = 1.0                         # alpha
    r4 = 1.0 # 10**np.random.uniform(0,1)   # kappa 
  if (cont==3):
    r3 = 1.0                          # alpha
    r4 = 1.0 #10**np.random.uniform(0,1)   # kappa 

  # newfolder = "./HW_data/HW_" + str(n) + "/data/"
  # file_path = newfolder + "BOUT.log.0"
  # with open(file_path, 'r') as file:
  #     content = file.read()
  #     if "finished" in content:
  #         print(r3,r4)
  
  if (n>=0):
    newfolder = "HW_data/HW_" + str(n)

    if (not os.path.isfile(newfolder + "/data/BOUT.dmp.0.nc")):
      cmd = ("cp -r HW " + newfolder)
      os.system(cmd)

      cmd = "sed -i s/AAA/" + str(r1) + "/g " + newfolder + "/data/BOUT.inp"
      os.system(cmd)

      cmd = "sed -i s/BBB/" + str(r2) + "/g " + newfolder + "/data/BOUT.inp"
      os.system(cmd)

      cmd = "sed -i s/CCC/" + str(r3) + "/g " + newfolder + "/data/BOUT.inp"
      os.system(cmd)

      cmd = "sed -i s/DDD/" + str(r4) + "/g " + newfolder + "/data/BOUT.inp"
      os.system(cmd)

      cmd = "cd " + newfolder + "; bsub < run.sh "
      os.system(cmd)
 

