import sys
import numpy as np
import matplotlib.pyplot as plt

import abaqus
import abaqusConstants

# Le path de python certaines distrib abaqus a l'air de ne pas contenir 
# le dossier qui contient le script en train d'être executé... 
# Donc on l'ajoute manuellement.
sys.path.append('C://temp/AbaqusLayupOptimizer')

import objective_functions

# Si le dataset n'est pas trouvé par le python d'abaqus
path = " C://temp/"

DOE = np.load(path + 'design_of_experience_1000.npy')
# DOE = np.load('design_of_experience_1000.npy')

# np.savetxt("layup_dataset.csv", DOE, delimiter=",")

results_of_DOE = np.zeros((DOE.shape[0], 2))

for i in range(DOE.shape[0]):
    odb = abaqus.session.openOdb(name= "job_automated_"+ str(i))
    results_of_DOE[i] = objective_functions.hashin(odb)
    
    # results_of_DOE[i] = np.random.random(2) # Pour les test
    # results_of_DOE[i] = [2*DOE[i][1], 5*DOE[i][3]] # Pour les test

    # Enregistrement a chaque iteration au cas ou ca crash
    np.save(f'results_of_doe_{str(DOE.shape[0])}', results_of_DOE)

print(results_of_DOE)