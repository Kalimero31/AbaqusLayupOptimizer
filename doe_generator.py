import sys
print(sys.path)
sys.path.append('//intram.ensam.eu/etudiants/paris/2020/2020-1214/config/appdata/python/python310/site-packages')
import numpy as np
from pyDOE import lhs

n_param = 9


doe = lhs(n_param, samples=2500)

doe_degrees = np.int32(np.round(doe*2)*45)

# print(type(doe_degrees[0][1]))
# print(doe_degrees[0])
# print(doe_degrees.shape)
# print(np.unique(doe_degrees, axis=0).shape)

unique_doe_degrees = np.unique(doe_degrees, axis=0)
shortened_doe_degrees = unique_doe_degrees[0:2000]

print(shortened_doe_degrees.shape)
print(np.unique(shortened_doe_degrees, axis=0).shape)
np.save("data/doe/design_of_experience_" + str(len(doe_degrees)) + ".npy", doe_degrees)

