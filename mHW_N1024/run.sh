#BSUB -J test
#BSUB -e test.err
#BSUB -o test.out
#BSUB -q scafellpikeSKL
#BSUB -n 1
#BSUB -R "span[ptile=16]"
#BSUB -W 48:00

python convert_2files.py
#python convert_netCDF2png.py
