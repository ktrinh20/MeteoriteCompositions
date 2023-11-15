"""
Goal:   Manage bulk elemental composition of meteorites and other (input) 
        compositions of interest.
        
Author: Kevin T. Trinh
"""

import periodictable as pt
import pandas as pd
import numpy as np

## DEFINE METEORITE BULK ELEMENTAL COMPOSITIONS

# carbonaceous chondrites
CI = [19.000, 5.448, 3.543, 9.714, 10.895, 0.505, 0.855, 0.928, 0.057, 0.012, 46.737, 2.006] # compiled by Melwani-Daswani et al. (2021)
CM = [21.731, 2.755, 2.244, 11.733, 12.957, 0.398, 1.153, 1.316, 0.038, 0.019, 44.073, 1.428] # compiled by Melwani-Daswani et al. (2021)
CV = [24.123, 2.258, 0.544, 14.679, 16.116, 0.349, 1.725, 1.889, 0.037, 0.005, 37.980, 0.287] # compiled by Melwani-Daswani et al. (2021)
CK = [23.379, 1.728, 0.224, 14.942, 16.060, 0.315, 1.494, 1.728, 0.029, 0.005, 39.802, 0.285] # compiled by Melwani-Daswani et al. (2021)
CR = [24.254, 1.937, 2.038, 13.961, 15.286, 0.336, 1.172, 1.315, 0.032, 0.007, 39.280, 0.319] # compiled by Melwani-Daswani et al. (2021)
CO = [25.391, 2.234, 0.447, 14.727, 16.047, 0.427, 1.422, 1.605, 0.037, 0.005, 37.578, 0.071] # compiled by Melwani-Daswani et al. (2021)

# comets
comet67P = [6.035, 1.789, 27.814, 0.985, 10.434, 0.696, 0.178, 0.082, 0.031, 0.031, 41.652, 11.283] # compiled by Melwani-Daswani et al. (2021)

# ordinary chondrites
H = [27.5, 0.20, 1.1, 14.0, 16.9, 0.64, 1.13, 1.25, 0.0780, 80e-4, 35.7, 0] # from Wasson et al. (1997)
L = [21.5, 0.22, 0.9, 14.9, 18.5, 0.70, 1.22, 1.31, 0.0825, 76e-4, 37.7, 0] # from Wasson et al. (1997)
LL = [18.5, 0.23, 1.2, 15.3, 18.9, 0.70, 1.19, 1.30, 0.0790, 130e-4, 40.0, 0] # from Wasson et al. (1997)

# enstatite chondrites
EH = [29.0, 0.58, 0.40, 10.6, 16.7, 0.68, 0.81, 0.85, 800e-4, 660e-4, 28.0, 0] # from Wasson et al. (1997)
EL = [22.0, 0.33, 0.36, 14.1, 18.6, 0.58, 1.05, 1.01, 735e-4, 210e-4, 31.0, 0] # from Wasson et al. (1997)

## NORMALIZE ELEMENTAL COMPOSITIONS W.R.T. IRON BY MASS AND MOLES
# normalize and store as dictionary
meteorite_class = ['CI', 'CM', 'CV', 'CK', 'CR', 'CO', 'H', 'L', 'LL', 'EH', 'EL', 'comet 67P']
comp_list = [CI, CM, CV, CK, CR, CO, H, L, LL, EH, EL, comet67P]
element_names = ['Fe', 'S', 'C', 'Mg', 'Si', 'Na', 'Al', 'Ca', 'K', 'Cl', 'O', 'H']
comp_dict = {} 
for i in range(len(meteorite_class)):
    tmp = np.array(comp_list[i])/sum(np.array(comp_list[i]))*100
    comp_dict[meteorite_class[i]] = tmp.tolist()

# convert to Pandas dataframe
df_mass = pd.DataFrame(comp_dict, index=element_names)

# also create a version that stores molar ratios!
Fe = pt.formula('Fe').mass
S = pt.formula('S').mass
C = pt.formula('C').mass
Mg = pt.formula('Mg').mass
Si = pt.formula('Si').mass
Na = pt.formula('Na').mass
Al = pt.formula('Al').mass
Ca = pt.formula('Ca').mass
K = pt.formula('K').mass
Cl = pt.formula('Cl').mass
O = pt.formula('O').mass
H = pt.formula('H').mass
molar_masses = np.array([Fe, S, C, Mg, Si, Na, Al, Ca, K, Cl, O, H])

df_molar = df_mass.copy()
for i in range(len(meteorite_class)):
    k = meteorite_class[i]
    df_molar[k] = df_mass[k]/molar_masses/sum(df_mass[k]/molar_masses)*100
    
# mass dataframe normalized to iron
df_mass_n = df_mass.copy()/df_mass.loc['Fe']
df_mass_n = df_mass_n.rename(index={'Fe': 'Fe/Fe', 
                                    'S': 'S/Fe',
                                    'C': 'C/Fe',
                                    'Mg': 'Mg/Fe', 
                                    'Si': 'Si/Fe', 
                                    'Na': 'Na/Fe',
                                    'Al': 'Al/Fe',
                                    'Ca': 'Ca/Fe',
                                    'K': 'K/Fe',
                                    'Cl': 'Cl/Fe',
                                    'O': 'O/Fe', 
                                    'H': 'H/Fe'})

df_molar_n = df_molar.copy()/df_molar.loc['Fe']
df_molar_n = df_molar_n.rename(index={'Fe': 'Fe/Fe', 
                                    'S': 'S/Fe',
                                    'C': 'C/Fe',
                                    'Mg': 'Mg/Fe', 
                                    'Si': 'Si/Fe', 
                                    'Na': 'Na/Fe',
                                    'Al': 'Al/Fe',
                                    'Ca': 'Ca/Fe',
                                    'K': 'K/Fe',
                                    'Cl': 'Cl/Fe',
                                    'O': 'O/Fe', 
                                    'H': 'H/Fe'})

## VIEW A COMPOSITION DATAFRAME
df_mass_n
#df_molar_n
