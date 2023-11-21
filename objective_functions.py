import sys
sys.path.append('C://temp/AbaqusLayupOptimizer')

import abaqus
import abaqusConstants
import matplotlib.pyplot as plt

import odb_field_extractor as odbFE

# Il faut coder de nouvelles fonctions objectives qui mettent en place les criteres de tsai-wu/hi

# Fonction objective d'un eleve de la promo d'avant
def objective_function_2022_1(odb):
    displacement = odbFE.get_field_data(odb, 'U')
    thickness = odbFE.get_field_data(odb, 'STH')

    val = max(displacement) * 10 / 6.913 
    + max(thickness) / 4

    return(val)

def objective_function_2023(odb):
    pass
    # On veut le max de displacement
if __name__ == "__main__":

# Exemple : Calcul de la fonction objective pour une odb existante.
    odb_name = "Job_test_vizu_4.odb"
    my_odb = abaqus.session.openOdb(name=odb_name)
    print(objective_function_2022_1(my_odb))

    


