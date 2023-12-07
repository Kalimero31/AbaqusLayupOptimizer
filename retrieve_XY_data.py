import abaqus
import abaqusConstants

odb = abaqus.session.openOdb(name= "combinaison_48.odb")

# last_step = odb.steps.values()[-1]
# last_frame = last_step.frames[-1]
# print(last_frame.fieldOutputs)

# Nom de la step
nom_step = 'load'  # Remplace par le nom de ta step

nodeIDs = [5, 6, 45,46,47,48,49,50,51,52,53]
nodeIDs = [1,2,3,4,5,6,7,8,9]

step = odb.steps[nom_step]
# for frame in step.frames:
for frame in [step.frames[-1]]:
    for i in nodeIDs:
        rf = frame.fieldOutputs['RF'].values[i]
        print(rf.data[0])

# Ferme l'ODB
odb.close()