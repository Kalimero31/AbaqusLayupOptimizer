import sys

# Le path de python certaines distrib abaqus a l'air de ne pas contenir 
# le dossier qui contient le script en train d'etre execute... 
# donc on l'ajoute manuellement.
sys.path.append('C://temp/2020-1214/AbaqusLayupOptimizer')

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

def hashin(odb):
    hashin_indexes = ['HSNFCCRT', 'HSNFTCRT', 'HSNMTCRT', 'HSNMCCRT']
    hashin_max_values = [max(odbFE.get_field_data(odb, i)) for i in hashin_indexes]

    max_failure = max(hashin_max_values)
    displacement = odbFE.get_field_data(odb, 'U')

    return([max_failure, displacement])

def objective_function_complete_failure(odb):
    # Une fonction qui prend en consideration la repartition des maximums de contrainte/failure. 
    # Car on prefere avoir du 1 quelque part plutot que du 0.9 partout (par exemple).
    pass

if __name__ == "__main__":

# Exemple : Calcul de la fonction objective pour une odb existante.
    odb_name = "Job_test_vizu_4.odb"
    my_odb = abaqus.session.openOdb(name=odb_name)
    print(objective_function_2022_1(my_odb))

    


