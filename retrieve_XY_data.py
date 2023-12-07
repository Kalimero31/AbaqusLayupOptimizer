import numpy as np
import abaqus
import abaqusConstants

essais_de_tractions = np.zeros((49,37))

nom_step = 'load'  # Remplace par le nom de ta step

for i in range(10):
    odb = abaqus.session.openOdb(name= "combinaison_"+str(i)+".odb")


    nodeIDs = [1,2,3,4,5,6,7,8,9]
    nodeIDs = [5, 6, 45,46,47,48,49,50,51,52,53]

    step = odb.steps[nom_step]

    sum_steps = []
    for j in range(len(step.frames)):
        sum = 0
        for i in nodeIDs:
            rf = step.frames[i].fieldOutputs['RF'].values[i-1]
            sum+= float(rf.data[0])
        essais_de_tractions[i,j] = sum

    odb.close()

np.save("C://temp/essais_de_tractions.npy", essais_de_tractions)