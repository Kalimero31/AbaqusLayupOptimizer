# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:09:57 2023

@author: 2021-1061
"""

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

# Un compositeLayupe est deja cree sur le modele
composite_layup = my_part.compositeLayups['CompositeLayup']
#region = my_part.sets['Set-1']


my_data = np.genfromtxt('Z:/Mes Documents/constitution-dataset-proprietes-pli/output_array.csv', delimiter=',')
properties_to_insert = my_data[4]
print('salss')

table = (my_data[4][0], properties_to_insert[1], 0.34, properties_to_insert[2], properties_to_insert[2], properties_to_insert[2])
# E1, E2, Nu12, G12, G13, G23
my_model.materials[my_material].elastic.setValues(table=(table, ))
