import sys
import numpy as np
import matplotlib.pyplot as plt

import abaqus
import abaqusConstants

# Le path de python certaines distrib abaqus a l'air de ne pas contenir 
# le dossier qui contient le script en train d'etre execute... 
# Donc on l'ajoute manuellement.
sys.path.append('C://temp/2020-1214/AbaqusLayupOptimizer')

import objective_functions

DOE = np.load('C://temp/2020-1214/AbaqusLayupOptimizer/design_of_experience_2000.npy')
# DOE = np.load('design_of_experience_1000.npy')

# np.savetxt("layup_dataset.csv", DOE, delimiter=",")

results_of_DOE = np.zeros((DOE.shape[0], 2))

for i in range(10):
    odb = abaqus.session.openOdb(name= "C://temp/job_automated_"+ str(i)+'.odb')
    print("hashin", type(objective_functions.hashin(odb)))
    print(len(results_of_DOE[0]))
    print("dataset row", type(results_of_DOE[0]))

    results_of_DOE[i] = np.array(objective_functions.hashin(odb))
    
    # results_of_DOE[i] = np.random.random(2) # Pour les test
    # results_of_DOE[i] = [2*DOE[i][1], 5*DOE[i][3]] # Pour les test

    # Enregistrement a chaque iteration au cas ou ca crash
    np.save('results_of_doe_' +str(DOE.shape[0]), results_of_DOE)

print(results_of_DOE)