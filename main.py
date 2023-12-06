import sys
import time

folder = "C://temp/AbaqusLayupOptimizer" #peridon
# folder = "C://temp/2020-1214/AbaqusLayupOptimizer" #mamouret
# folder = "C://temp/2020-1227/AbaqusLayupOptimizer" #esposito
# folder = "C://temp/2021-1061/AbaqusLayupOptimizer" #guilloux
# folder = "C://temp/2021-0606/AbaqusLayupOptimizer" #liber

sys.path.append(folder)
print(sys.path)



import abaqus_utils
import numpy as np
import abaqus
import csv

#import src.abaqus_utils as abaqus_utils 
#import src.odb_field_extractor as odb_field_extractor 

# On charge le plan d'experience (DOE). 
# Ce plan d'experience a ete genere par le script doe_generator.py
# Il contient une liste de combinaisons de 9 parametres.
# Exemple: [[0, 0, 0, 45, 45, 45, 90, 90, 90], etc...]
#MyDOE = np.load(folder + "/data/design_of_experience_2000.npy")

# Liens entre modele et parts de notre .cae
versions = [('1_plaque_plane', 'plaque_plane'),
            ('2_plaque_plane', 'plaque_plane'),
            ('3_tube', 'tube')]



#      Informations

k = 0 # pour le tube en 3D
model_name = versions[k][0]
part_name = versions[k][1]


#   Retrieving useful objets

models = abaqus.mdb.models

my_model = models[model_name]
my_part = my_model.parts[part_name]
my_material = 'composite'


my_data = np.genfromtxt('output_array.csv', delimiter=',')

for i in range(len(my_data)):
    properties_to_insert = my_data[i]

    table = (properties_to_insert[4][0], properties_to_insert[1], 0.34, properties_to_insert[2], properties_to_insert[2], properties_to_insert[2])
    # E1, E2, Nu12, G12, G13, G23
    my_model.materials[my_material].elastic.setValues(table=(table, ))
    abaqus_utils.submit_job("combinaison_"+ str(i), my_model)
    print(i)
