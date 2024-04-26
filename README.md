# Dust Model Visualization

This Python script provides visualization and analysis tools for studying the dust emission properties of astronomical sources. It includes functions for calculating modified black body spectra and plotting observational data alongside model predictions.

## Requirements

- Python 3.x
- numpy
- matplotlib
- seaborn
- astropy

Additionally, the `show_emlines` package is required for displaying emission lines, which can be installed from [here](https://github.com/aayush3009/show_emlines).

## Usage

1. Clone the repository:

```
git clone https://github.com/aayush3009/dust_SED_submm.git
cd dust_SED_submm
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Python script:

```
python ALMA_dust_SED.py
```


4. The script will generate a plot showing the modeled dust emission alongside observed data points.

## Description

### Main Script: `ALMA_dust_SED.py`

- The script defines functions for calculating modified black body spectra (`B_nu` and `I_nu`) and visualizing dust emission models.
- It utilizes the `astropy` library for cosmological calculations and units handling.
- Continuum detections for a radio galaxy (TNJ1338) at a specific redshift are used as observational data.
- Dust model parameters (mass, temperature, and spectral index) are provided to generate the model spectra.

### Additional Information

- `ALMA_band_start` and `ALMA_band_end` define the frequency ranges for ALMA bands.
- The `show_emlines` package is utilized to display ALMA lines in the plot.


