import numpy as np
import matplotlib.pyplot as plt
   
(ttime, Energy) = np.loadtxt("./HW_N256/energy_vs_time.txt",dtype="float64",unpack=True)
plt.plot(ttime, Energy, label="HW $256^2$")

(ttime, Energy) = np.loadtxt("./HW_N512/energy_vs_time.txt",dtype="float64",unpack=True)
plt.plot(ttime, Energy, label="HW $512^2$")

(ttime, Energy) = np.loadtxt("./mHW_N1024/energy_vs_time.txt",dtype="float64",unpack=True)
plt.plot(ttime, Energy, label="mHW $1024^2$")

plt.yscale("log")

plt.xlabel(r"time [$\omega^{-1}_i$]")
plt.ylabel(r"$\mathcal{F} (\phi)$")

plt.legend(frameon=False)
plt.savefig('energy_vs_time.png')
plt.close()



plt.xscale("log")
plt.yscale("log")

(k, Energy) = np.loadtxt("./HW_N256/energy/Spectrum_1000.txt",dtype="float64",unpack=True)
plt.plot(k, Energy, label="HW $256^2$")

(k, Energy) = np.loadtxt("./HW_N512/energy/Spectrum_1000.txt",dtype="float64",unpack=True)
plt.plot(k, Energy, label="HW $512^2$")

(k, Energy) = np.loadtxt("./mHW_N1024/energy/Spectrum_100.txt",dtype="float64",unpack=True)
plt.plot(k, Energy, label="mHW $1024^2$")

plt.xlabel(r"$k$ $[\rho^{-1}_i]$")
plt.ylabel(r"$\mathcal{F} (\phi)$")

plt.legend(frameon=False)
plt.savefig('spectra.png')
plt.close()
