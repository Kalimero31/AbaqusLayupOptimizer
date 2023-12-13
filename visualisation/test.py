import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from stl import mesh

# Charger le fichier STL
your_mesh = mesh.Mesh.from_file('ton_fichier.stl')

# Imaginons que tu as une liste de contraintes pour chaque triangle
# Remplace ceci par tes vraies données de contrainte
contraintes = np.random.rand(len(your_mesh.vectors))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parcourir les triangles et les dessiner avec la couleur correspondant à la contrainte
for i, vect in enumerate(your_mesh.vectors):
    triangle = [list(vect[0]), list(vect[1]), list(vect[2]), list(vect[0])]
    tri = np.array(triangle)
    
    # Choix de la couleur en fonction de la contrainte
    couleur = cm.jet(contraintes[i])

    ax.add_collection3d(plt.Poly3DCollection([tri], color=couleur))

# Mise en forme du graphique
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Afficher la colormap
mappable = cm.ScalarMappable(cmap=cm.jet)
mappable.set_array(contraintes)
plt.colorbar(mappable, shrink=0.5, aspect=5)

plt.show()
