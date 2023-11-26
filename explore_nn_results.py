import numpy as np
import matplotlib.pyplot as plt

U = np.load("archives/test_datasets/U.npy")
hashin = np.load("archives/test_datasets/hashin.npy")

plt.hist(U, bins=25)
# plt.show()

print(U)


plt.hist(U, bins=25)
plt.title('Histogramme des données')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.show()