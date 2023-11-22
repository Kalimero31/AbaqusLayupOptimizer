import sys
print(sys.path)
sys.path.append('//intram.ensam.eu/etudiants/paris/2020/2020-1214/config/appdata/python/python310/site-packages')
import numpy as np
from pyDOE import lhs

n_param = 9


doe = lhs(n_param, samples=2000)

doe_degrees = np.round(doe*2)*45
np.save("design_of_experience_" + str(len(doe_degrees)) + ".npy", doe_degrees)

