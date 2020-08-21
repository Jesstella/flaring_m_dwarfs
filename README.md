# flaring_m_dwarfs
Project code for work determining if flaring M dwarfs are the real culprits in the observed G dwarf super flares.

To recreate this sample: Each of the TRILEGAL module files contains the stars for one of the Kepler modules. The file trilegal_settings.txt contains the settings used in the TRILEGAL 1.6 input form, along with the coordinates used for the Kepler modules. The subsequent downloaded files need to be combined into one master file for use in this code. 

The catalog for Mathur et al. 2017 and Shibayama et al. 2013 will be needed to run this code, along with the Kepler magnitudes for this sample of stars (found at MAST). 

In this package there are two copies of each piece of code, one in the form of an executable .py file, and one in the form of a ipython notebook, which better describes the output. Each piece of code will do what is required to the sample and also produce plots to check the work. The order in which to use the files and a brief description of them is as follows: 

1) To cut the large TRILEGAL sample down to only those stars seen in Kepler use trilegal_cut_to_mathur.py.
2) To cut the Kepler sample down to just include G dwarfs like those seen in Shibayama et al. 2013, use cut_trilegal_to_shibayama.py.
3) To randomly choose a sample of these G dwarfs to contain binaries and to give these binary companions parameters use add_binaries_with_parameters.py.
4) To cut this sample of binaries down to only those with G dwarf primaries and M secondaries use cut_to_m_dwarfs.py.



