import sys
sys.path.append('C://temp/AbaqusLayupOptimizer')

import numpy as np
import abaqus

import abaqus_utils as abaqus_utils 
import odb_field_extractor as odb_field_extractor 

MyDOE = np.load("plan_of_experience_1000.npy")

# Liens entre modele et parts de notre .cae
versions = [('1_plaque_plane', 'plaque_plane'),
            ('2_plaque_plane', 'plaque_plane'),
            ('3_tube', 'tube')]



#      Informations

k = 2
model_name = versions[k][0]
part_name = versions[k][1]


#   Retrieving useful objets

models = abaqus.mdb.models
my_model = models[model_name]
my_part = my_model.parts[part_name]
my_material = 'composite'


# faces = my_part.faces.getSequenceFromMask(mask=('[#1 ]', ), )
# print(my_part.sets)

composite_layup = my_part.compositeLayups['CompositeLayup']
region = my_part.sets['Set-1']


for i in range(1):
    print(str(i))
    strat_exemple = MyDOE[0]
    abaqus_utils.make_stratification(strat_exemple)
    abaqus_utils.submit_job(my_model, "job_automated_"+ str(i))


