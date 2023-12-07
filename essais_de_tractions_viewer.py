import matplotlib.pyplot as plt
import numpy as np

edt = np.load('essais_de_tractions.npy')

print(edt.shape)

print(edt)

row0 = edt[-1]
plt.plot(row0)
plt.show()
