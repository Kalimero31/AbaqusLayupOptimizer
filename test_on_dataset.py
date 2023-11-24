import numpy as np
import matplotlib.pyplot as plt

output_array = np.load('datasets/800_simulations_22-11-23 (1 error)/results_of_doe_22-11.npy')

U = output_array[:,0]
hashin = output_array[:,1]

print(U.shape)

print(np.mean(U))
print(np.mean(hashin))

plt.hist(U, bins=25)  # Tu peux ajuster le nombre de 'bins' selon le besoin
plt.title('Histogramme des données')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.show()