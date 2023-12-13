import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh

# Charger le fichier STL
votre_mesh = mesh.Mesh.from_file('C:/Users/jimit/OneDrive/Documents\8. CAO/AC_68/Pièces/Hull/Boat.STL')

# Créer une figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ajouter les vecteurs du mesh à la visualisation
ax.add_collection3d(Poly3DCollection(votre_mesh.vectors))

# Auto échelle des axes
scale = votre_mesh.points.flatten('C')

ax.auto_scale_xyz(scale, scale, scale)

# Montrer la figure
plt.show()
