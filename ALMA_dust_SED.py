import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
sn.set_palette("Spectral", 10)

from astropy.cosmology import Planck18 as cosmo
import astropy.units as u

from dust_emissivity.fit_sed import fit_modified_bb

# Custom emission line package, needs to be installed separately from: https://github.com/aayush3009/show_emlines
from show_emlines import show_lines as sl

# Define the modified black body function. Taken from: https://github.com/hw2814/dust-SED-pymc3#

# Planck function
def B_nu(nu, T):
    c = 3.0e8
    k = 1.380649e-23
    h = 6.62607015e-34

    return(((2*h*nu**3)/(c**2)) * (1/(np.exp((h*nu)/(k*T)) - 1))*u.erg/u.s/u.cm**2/u.steradian/u.Hz)

# Modified BB
def I_nu(nu, T, beta, Mdust, redshift):
    Mdust_g = (Mdust*u.solMass).to(u.g)
    kappa0 = (0.192*(u.m**2/u.kg)).to(u.cm**2/u.g)
    nu_0 = 100e9 # reference frequency, fixed at 100 GHz
    kappa = kappa0 * (nu/nu_0)**beta
    
    lum_dist = cosmo.luminosity_distance(redshift).to(u.cm)
    intensity = ((1+redshift)/(4*np.pi/u.steradian*lum_dist**2)) * Mdust_g * kappa * B_nu(nu, T)

    intensity_mjy = intensity.to(u.mJy, equivalencies=u.spectral_density(nu*u.Hz))
    
    return(intensity_mjy)

### ALMA bands frequency range
ALMA_band_start = np.array([35, 67, 84, 125, 163, 211, 275, 385, 602, 787])*1e9
ALMA_band_end = np.array([50, 116, 116, 163, 211, 275, 373, 500, 720, 950])*1e9


### Set up the source properties and dust model parameters

### Continuum detections for radio galaxy TNJ1338 at z=4.1

freq = np.array([100e9, 250e9, 352.7e9, 666.2e9]) * u.Hz
flux = np.array([0.18, 6.2, 10.1, 21.4]) * u.mJy

# Change flux units to cgs if needed
# flux_cgs = (flux*u.mJy).to(u.erg/u.s/u.cm**2/u.Hz, equivalencies=u.spectral_density(freq))

# Source redshift
redshift = 4.110

# Dust model parameters (no need to assign units here, this is taken care of in the Planck function
dust_mass = 8e10 # Dust mass
T1 = 60. # Dust temperature
beta1 = 1.5 # Beta
# Calculate dust SED
intensity1 = I_nu(frequencies, T1, beta1, dust_mass, redshift)


### Show the dust model
# Define your own frequency range as needed
frequencies = np.linspace(200, 7000, 500)*1e9

plt.close()
fig = plt.figure(figsize=(6,5))
plt.grid(alpha=0.4)

# plt.plot(frequencies/(1+redshift), intensity1*(1+redshift), c='C1', ls='-', lw=2, 
#          label=rf"$\beta = {beta1}, T_d = {T1}$ K")

plt.plot(frequencies/(1+redshift), intensity1*(1+redshift), c='C1', ls='--', lw=2, 
        label=rf"$\beta = {beta2}, T_d = {T2}$ K")

## Data
plt.scatter(freq, flux, marker='s', s=100, zorder=12, label=r"Cont. detections")

### Plot ALMA lines from the show_emlines package
sl.show_ALMA_lines(sl.ALMA_ISM_lines[2:4], sl.ALMA_ISM_line_names[2:4], redshift, ypos=1e-1, fontsize=13, lnames=True)

### Show ALMA bands
for i in range(len(ALMA_band_start)):
    plt.axvspan(ALMA_band_start[i], ALMA_band_end[i], color=f'C{i}', alpha=0.3)

plt.xscale('log')
plt.yscale('log')

plt.figtext(0.2, 0.76, rf"$z={redshift}$", fontsize=13)

plt.xlabel(r"$\nu_{\mathrm{obs}}$ [GHz]", fontsize=14)
plt.ylabel(r"$S_\nu$ [mJy]", fontsize=14)

# plt.xticks([5e10, 1e11, 2e11, 3e11, 5e11, 1000e9], ["50", "100", "200", "300", "500", "1000"], fontsize=13)
# plt.yticks([1e-3, 1e-2], ["0.001", "0.01"], fontsize=13)

# plt.xlim(9e10, 9e11)
# plt.ylim(1e-6, 1e-2)

plt.legend()

plt.tight_layout()

plt.show()
