import numpy as np
from pyDOE import lhs

n_param = 9


poe = lhs(n_param, samples=1000)
poe_degrees = np.round(poe*2)*45

np.save("design_of_experience_" + str(len(poe_degrees)) + ".npy", poe_degrees)

