#Necessary modules 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import random
import csv

#Paths 
data_path = '/Users/Jess/699-2/final_github_code/'
mathur_path = '/Users/Jess/699-2/mathur_2017/'
trilegal_path = '/Users/Jess/699-2/trilegal_data/'

#Checking the current sample
data = pd.read_csv(data_path + 'final_sample.csv')
teff = pd.read_csv(data_path + 'final_sample.csv')['logTe']
logg = pd.read_csv(data_path + 'final_sample.csv')['logg']
kep_mag = pd.read_csv(data_path + 'final_sample.csv')['Kepler']
print('Number of stars in the final sample: ' + str(len(kep_mag)))
plt.figure(figsize=(20, 4))
plt.subplot(131)
plt.hist(teff, color='#fbb4ae')
plt.ylabel('N', fontsize=15)
plt.xlabel(r'$T_{eff}$', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.subplot(132)
plt.hist(logg, color='#b3cde3')
plt.title(str(len(kep_mag)) + ' total stars', fontsize=15)
plt.xlabel('logg', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.subplot(133)
plt.hist(kep_mag, color='#ccebc5')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Kepler Magnitude', fontsize=15)
plt.savefig(data_path + 'histograms_whole_sample_to_mathur.png')

#Cutting sample down to G stars
g_stars = data[(data["logTe"] >= np.log10(5100)) & (data["logTe"] <= np.log10(6000)) & (data['logg'] >= 4)]   
print('Number of G stars in the binary sample: ' + str(len(g_stars['logTe'])))
print('Number of stars in the Shibayama sample: 80000')
np.savetxt(data_path + 'g_stars.csv', g_stars, delimiter=',', header='Index,Gc,logAge,M_H,m_ini,logL,logTe,logg,m-M0,Av,m2/m1,mbol,Kepler,g,r,i,DDO51_finf,Mact,z.1')

#Check the G stars against the Mathur stars
g_stars = pd.read_csv(data_path + 'g_stars.csv')
teff_g = pd.read_csv(data_path + 'g_stars.csv')['logTe']
logg_g = pd.read_csv(data_path + 'g_stars.csv')['logg']
kep_mag_g = pd.read_csv(data_path + 'g_stars.csv')['Kepler']

mathur = pd.read_csv(mathur_path + 'mathur_2017_edited.txt', delimiter='|') 

g_stars_mathur = mathur[(mathur["Teff"] >= 5100) & (mathur["Teff"] <= 6000) & (mathur['log(g)'] >= 4)]   
print('Number of G stars in M17: ' + str(len(g_stars_mathur['Teff'])))
print('Number of stars in the Shibayama sample: 80000')
teff_mathur = g_stars_mathur['Teff']
logg_mathur = g_stars_mathur['log(g)']

plt.figure(figsize=(15, 4))
plt.subplot(121)
plt.hist(teff_g, color='#a50026', histtype='step', linewidth=4, label='G Stars')
plt.hist(np.log10(teff_mathur), histtype='step', linewidth=4, color='#f46d43', label='M17 - G Stars', linestyle='-.')
plt.title(str(len(kep_mag_g)) + ' total stars', fontsize=15)
plt.ylabel('N', fontsize=15)
plt.xlabel(r'$T_{eff}$', fontsize=15)
plt.legend(loc=2, fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.subplot(122)
plt.hist(logg_g, histtype='step', linewidth=4, color='#a50026')
plt.hist(logg_mathur, histtype='step', linewidth=4, color='#f46d43', linestyle='-.')
plt.xlabel('logg', fontsize=15)
plt.xticks(fontsize=15)
plt.yscale('log')
plt.yticks(fontsize=15)
plt.savefig(data_path + 'histograms_g_stars_to_shibayama.png')

#Adding binaries to the data 
binaries = g_stars.sample(frac=0.44014209591474255, replace=False)
print("Number of binaries in the sample: " + str(len(binaries))) # Print number of binaries in the sample
plt.figure(figsize=(15, 4))
plt.subplot(131)
plt.hist(binaries['logTe'], histtype='step', color='#a6dba0', linewidth=4, label='G Star Binaries')
plt.hist(teff_g, histtype='step', linewidth=4, linestyle='-.', label='All G Stars', color='#1b7837')
plt.ylabel('N', fontsize=15)
plt.legend(loc=2, fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.yscale('log')
plt.xlabel(r'$T_{eff}$', fontsize=15)
plt.subplot(132)
plt.title(str(len(binaries)) + ' binary stars', fontsize=15)
plt.hist(binaries['logg'], histtype='step', color='#a6dba0', linewidth=4)
plt.hist(logg_g, histtype='step', linewidth=4, linestyle='-.', color='#1b7837')
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.xlabel('logg', fontsize=15)
plt.yscale('log')
plt.subplot(133)
plt.hist(binaries['Kepler'], histtype='step', color='#a6dba0', linewidth=4)
plt.hist(kep_mag_g, histtype='step', linewidth=4, linestyle='-.', color='#1b7837')
plt.xlabel('Kepler Magnitude', fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.yscale('log')
plt.savefig(data_path + 'g_stars_comparison_binaries')
np.savetxt(data_path + 'G_with_binaries.csv', binaries, delimiter=',', header='Index,Gc,logAge,M_H,m_ini,logL,logTe,logg,m-M0,Av,m2/m1,mbol,Kepler,g,r,i,DDO51_finf,Mact,z.1')

def period_of_binary(num_of_stars): 
    mu, sigma = 5.03, 2.28 
    distribution = np.random.normal(mu, sigma, num_of_stars) 
    period = random.choice(distribution)  
    return period 

def mass_ratio_of_binary(num_of_stars): 
    mass_ratio = random.uniform(0.1, 1) 
    return mass_ratio 

binaries = pd.read_csv(data_path + 'G_with_binaries.csv')

periods = [] 
mass_ratios = [] 

for i in range(0, len(binaries['# Index'])): 
    period = period_of_binary(1000) 
    mass_ratio = mass_ratio_of_binary(1000) 
    periods.append(period)
    mass_ratios.append(mass_ratio)

#Save a new CSV file with all the columns 
full_sample_array = np.column_stack((binaries,periods,mass_ratios))
np.savetxt(data_path + 'G_with_binaries_with_parameters.csv', full_sample_array, delimiter=',', header='Index,Gc,logAge,M_H,m_ini,logL,logTe,logg,m-M0,Av,m2/m1,mbol,Kepler,g,r,i,DDO51_finf,Mact,z.1,periods,mass_ratios')
binaries_with_parameters = pd.read_csv(data_path + 'G_with_binaries_with_parameters.csv')

#Testing the mass ratios and periods
numbers = np.linspace(0, 100000, 100000)
print(len(binaries_with_parameters))
test_periods = []
test_mass_ratios = []
for i in numbers:
    a = period_of_binary(10000)
    test_periods.append(a)
for i in numbers: 
    a = mass_ratio_of_binary(10000)
    test_mass_ratios.append(a)

plt.figure(figsize=(15, 4))
plt.subplot(121)
plt.hist(test_periods, histtype='step', label='Test Periods', color='#8c510a', linewidth=4, linestyle='-.')
plt.hist(periods, histtype='step', label='Sample Periods', color='#dfc27d', linewidth=4)
plt.legend(loc=2, fontsize=15)
plt.ylabel('N', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Period [days]', fontsize=15)
plt.yscale('log')
plt.subplot(122)
plt.hist(test_mass_ratios, histtype='step', color='#8c510a', linewidth=4, linestyle='-.')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Mass Ratio', fontsize=15)
plt.hist(mass_ratios, histtype='step', color='#dfc27d', linewidth=4)
plt.savefig(data_path + 'period_mass_ratio.png') 

#Secondary mass
g_binaries = pd.read_csv(data_path + 'G_with_binaries_with_parameters.csv')

m2_m1 = pd.read_csv(data_path + 'G_with_binaries_with_parameters.csv')['mass_ratios']
m_act = pd.read_csv(data_path + 'G_with_binaries_with_parameters.csv')['Mact']
m2 = m2_m1 * m_act
full_sample_array = np.column_stack((g_binaries,m2))

np.savetxt(data_path + 'G_with_binaries_with_parameters_2.csv', full_sample_array, delimiter=',', header='Index,Gc,logAge,M_H,m_ini,logL,logTe,logg,m-M0,Av,m2/m1,mbol,Kepler,g,r,i,DDO51_finf,Mact,z.1,periods,mass_ratios,sec_mass')

#Testing secondary masses
bins_with_sec_masses = pd.read_csv(data_path + 'G_with_binaries_with_parameters_2.csv')
plt.figure(figsize=(10, 7))
plt.scatter(bins_with_sec_masses['Mact'], bins_with_sec_masses['sec_mass'], c=bins_with_sec_masses['mass_ratios'], s=0.5)
plt.xlabel(r'Primary Mass $M_{\odot}$', fontsize=15)
plt.ylabel(r'Secondary Mass $M_{\odot}$', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.colorbar()
plt.savefig(data_path + 'secondary_masses.png')

#Secondary composition and temperature 
teff = pd.read_csv(data_path + 'final_sample.csv')['logTe'] #Primary temp
comp = pd.read_csv(data_path + 'final_sample.csv')['[M/H]'] #Primary comp
mass = pd.read_csv(data_path + 'final_sample.csv')['Mact'] #Primary mass
sec_mass = pd.read_csv(data_path + 'G_with_binaries_with_parameters_2.csv')['sec_mass']
full_sample = pd.read_csv(data_path + 'G_with_binaries_with_parameters_2.csv')

sec_mass = list(sec_mass)
mass = list(mass)
teff = list(teff)
final_temperature_list = []
final_composition_list = []
temperature_list = []
composition_list = []

print('running')

for i in sec_mass:

    sec_mass_compare = min(mass, key=lambda x:abs(x-i))
    idx = mass.index(sec_mass_compare)
    sec_comp = comp[idx]
    sec_temp = teff[idx]
    final_temperature_list.append(sec_temp)
    final_composition_list.append(sec_comp)

#Testing secondary temperature and composition 
plt.figure(figsize=(15, 4))
plt.subplot(121)
plt.hist(final_temperature_list, edgecolor='black', color='white', linewidth=2)
plt.xlabel(r'Secondary log($T_{eff}$)', fontsize=15)
plt.ylabel('N', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.subplot(122)
plt.hist(final_composition_list, edgecolor='black', color='white', linewidth=2)
plt.xlabel('Secondary [M/H]', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig(data_path + 'secondary_temp_and_comp.png')

full_sample_array = np.column_stack((full_sample,final_temperature_list,final_composition_list))
np.savetxt(data_path + 'G_with_binaries_with_parameters_3.csv', full_sample_array, delimiter=',', header='Index,Gc,logAge,M_H,m_ini,logL,logTe,logg,m-M0,Av,m2/m1,mbol,Kepler,g,r,i,DDO51_finf,Mact,z.1,periods,mass_ratios,sec_mass,sec_temp,sec_comp')

#Cut down to M dwarf secondaries
sample = pd.read_csv(data_path + 'G_with_binaries_with_parameters_3.csv')
rows = sample[(sample["sec_temp"] <= np.log10(4000))]
print('There are ' + str(len(rows['logTe'])) + ' G/M binaries in this sample.')
rows.to_csv(data_path + 'final_sample_gm_binaries.csv') # Save to a new CSV file

trilegal_sample = pd.read_csv(trilegal_path + 'trilegal_master.csv') 
print('There are ' + str(len(trilegal_sample['logTe'])) + ' stars in the TRILEGAL sample.')
full_sample = pd.read_csv(data_path + 'final_sample.csv')
print('There are ' + str(len(full_sample['logTe'])) + ' stars in the total sample.')
binaries = pd.read_csv(data_path + 'g_stars.csv')
print(str(len(binaries['logTe'])) + ' of these are G stars.')
g_stars = pd.read_csv(data_path + 'G_with_binaries.csv')
print(str(len(g_stars['logTe'])) + ' of these are binaries.')
g_m_binaries = pd.read_csv(data_path + 'final_sample_gm_binaries.csv')
print(str(len(g_m_binaries['logTe'])) + ' of these G primaries have an M companion.')

complete_list = [str(len(trilegal_sample['logTe'])) + ' & ' + str(len(full_sample['logTe'])) + ' & ' + str(len(binaries['logTe'])) + ' & ' + str(len(g_stars['logTe'])) + ' & ' + str(len(g_m_binaries['logTe']))]
np.savetxt(data_path + 'final_statistics.txt', complete_list, fmt='%s', delimiter='&', comments='', header='TRILEGAL & Total Sample & Binaries & G Type Primaries & G/M Binaries')
