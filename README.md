# flaring_m_dwarfs
Project code and data for work determining if flaring M dwarfs are the real culprits in the observed G dwarf super flares.

Each of the TRILEGAL module files contains the stars for one of the Kepler modules, they are numbered consistent with the labelling of the modules seen in the paper. 

These will need to be combined into one master file for use in this code. 

Mathur 2017 files will also be needed to run this code, along with the Kepler magnitudes for this sample of stars (found at MAST). 

CODE FILES: 
1) To compare the TRILEGAL sample to the M17 sample, use trilegal_cut_to_mathur. 
Output:
- Plot showing the density of stars binned by temperature, logg and kepler magnitude for the M17 sample.
- Plot showing the density of stars binned by temperature, logg and kepler magnitude for the TRILEGAL sample. 
- Final sample file for stellar population. 
- Comparison histograms between the TRILEGAL sample, the M17 sample and the outputted stellar population as a function of temperature, logg and Kepler magnitude. 

2) To check that there are not to many repeats in the TRILEGAL sample and that it has roughly the same amount of stars as the Shibayama (2013) sample, use check_sample_for_repeats.py. 
Output: 
- The size of the sample and the size of the Shibayama sample. 
- The amount of stars which show repeats.
- The percentage of the sample which has a repeating star. 
- Which star has the most repeats.
- Plot showing a histogram of how many stars repeat as a function of how often they repeat. 
- Two HR diagrams (logg vs. teff) showing the amount of repeats in a star as color. 
- Two histograms of the samples overplotted along with vertical lines anywhere there may be an anomaly in the data (manually inputted). 

3) To cut the sample down to just contain G/M binaries as would have been seen in the Shibayama sample, use full_code_sample_to_cut.py 
Output: 
- Histograms in temp, logg and Kepler magnitude at the M17 cut stage, before the sample is cut to Shibayama or binaries added. 
- File containing the stars, cut to the Shibayama sample, so only G stars consistent with their parameters remain. 
- Double histogram of this new G star sample comparing it with the Mathur data cut to the same parameters. 
- Number of binaries in the sample, once it is cut for binarity. 
- Triple histogram in temp, logg and Kepler magnitude comparing the parameters of the G star sample as a whole to those chosen to be binary systems - ensures the random nature of choosing the binaries. 
- File containing just the G stars chosen to be in binary systems. 
- File containing the G stars chosen to be binary systems and also the companion mass ratio and period. 
- Double histogram showing the period and mass ratio of the binary companions compared with a random distribution over an order of magnitude more randomly chosen stars to ensure random nature of choosing period and mass ratio. 
- File with all of the above and secondary mass added. 
- Scatter plot of secondary mass versus primary mass for the binary systems. 
- Double histogram showing secondary temperature and secondary composition. 
- File with all of the above but including secondary temperature and composition.
- File with all of the above but only including systems whose binary stars are M dwarfs. 
- Number of G/M binaries in the sample. 
- File containing final statistics.
