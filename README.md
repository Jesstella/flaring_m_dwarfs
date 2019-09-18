# flaring_m_dwarfs
Project code for work determining if flaring M dwarfs are the real culprits in the observed G dwarf super flares.

Each of the TRILEGAL module files contains the stars for one of the Kepler modules. The file trilegal_settings.txt contains the settings used in the TRILEGAL 1.6 input form, along with the coordinates used for the Kepler modules.

These will need to be combined into one master file for use in this code. 

Mathur 2017 files will also be needed to run this code, along with the Kepler magnitudes for this sample of stars (found at MAST). 

CODE FILES: 
1) To compare the TRILEGAL sample to the M17 sample, use trilegal_cut_to_mathur. 
Output:
- Plot showing the density of stars binned by temperature, logg and kepler magnitude for the M17 sample.
- Plot showing the density of stars binned by temperature, logg and kepler magnitude for the TRILEGAL sample. 
- Final sample file for stellar population. 
- Comparison histograms between the TRILEGAL sample, the M17 sample and the outputted stellar population as a function of temperature, logg and Kepler magnitude. 

2) To cut the sample down to just contain G/M binaries as would have been seen in the Shibayama sample, use full_code_sample_to_cut.py 
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

Using the first set up described in the paper we get the following results: 
- Number of G dwarfs in sample = 82470 
- Number of these G dwarfs which have binaries = 36299
- Number of these binary systems with G dwarf primaries, which also have an M star secondary = 18735
