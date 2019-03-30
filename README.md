# flaring_m_dwarfs
Project code and data for work determining if flaring M dwarfs are the real culprits in the observed G dwarf super flares.

Each of the TRILEGAL module files contains the stars for one of the Kepler modules, they are numbered consistent with the labelling of the modules seen in the paper. 

These will need to be combined into one master file for use in this code. 

Mathur 2017 files will also be needed to run this code, along with the Kepler magnitudes for this sample of stars (found at MAST). 

CODE FILES: 
1) To compare the TRILEGAL sample to the M17 sample use trilegal_cut_to_mathur. 
Output:
- Plot showing the density of stars binned by temperature, logg and kepler magnitude for the M17 sample.
- Plot showing the density of stars binned by temperature, logg and kepler magnitude for the TRILEGAL sample. 
- Final sample file for stellar population. 
- Comparison histograms between the TRILEGAL sample, the M17 sample and the outputted stellar population as a function of temperature, logg and Kepler magnitude. 

