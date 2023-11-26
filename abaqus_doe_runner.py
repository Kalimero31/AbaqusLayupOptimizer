import sys
import time

# Le path de python certaines distrib abaqus a l'air de ne pas contenir 
# le dossier qui contient le script en train d'etre execute... 
# donc on l'ajoute manuellement.

folder = "C://temp/2020-1214/AbaqusLayupOptimizer" #mamouret
# folder = "C://temp/2020-1227/AbaqusLayupOptimizer" #esposito
# folder = "C://temp/2021-1061/AbaqusLayupOptimizer" #guilloux
# folder = "C://temp/2021-0606/AbaqusLayupOptimizer" #liber

sys.path.append(folder)

import numpy as np
import abaqus

import src.abaqus_utils as abaqus_utils 
import src.odb_field_extractor as odb_field_extractor 

# On charge le plan d'experience (DOE). 
# Ce plan d'experience a ete genere par le script doe_generator.py
# Il contient une liste de combinaisons de 9 parametres.
# Exemple: [[0, 0, 0, 45, 45, 45, 90, 90, 90], etc...]
MyDOE = np.load(folder + "/data/design_of_experience_2000.npy")

# Liens entre modele et parts de notre .cae
versions = [('1_plaque_plane', 'plaque_plane'),
            ('2_plaque_plane', 'plaque_plane'),
            ('3_tube', 'tube')]



#      Informations

k = 2 # pour le tube en 3D
model_name = versions[k][0]
part_name = versions[k][1]


#   Retrieving useful objets

models = abaqus.mdb.models

my_model = models[model_name]
my_part = my_model.parts[part_name]
my_material = 'composite'

# Un compositeLayupe est deja cree sur le modele
composite_layup = my_part.compositeLayups['CompositeLayup']
region = my_part.sets['Set-1']

t = time.time()

# Boucle principale de calcul sur tous les elements du DOE
# for i in range(len(MyDOE)):

for i in range(0, 500):
# for i in range(500, 1000):
# for i in range(1000, 1500):
# for i in range(1500, 2000):
    strat_exemple = MyDOE[i]
    abaqus_utils.make_stratification(composite_layup, region, my_material, strat_exemple)
    abaqus_utils.submit_job("automated_"+ str(i), my_model)

    # Affichage du temps pour chaque essai
    t1 = time.time()
    print('Essai ', str(i) , ' : ' , {str(t1-t)} , ' s')
    t = t1


