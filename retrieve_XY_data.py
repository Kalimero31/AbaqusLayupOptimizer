import abaqus
import abaqusConstants

odb = abaqus.session.openOdb(name= "combinaison_48.odb")

# last_step = odb.steps.values()[-1]
# last_frame = last_step.frames[-1]
# print(last_frame.fieldOutputs)

# Nom de la step
nom_step = 'load'  # Remplace par le nom de ta step

nodeID = 5

step = odb.steps[nom_step]
# for frame in step.frames:
frame = step.frames[-1]
rf = frame.fieldOutputs['RF'].values[0]
# rf = frame.fieldOutputs['RF'].values.magnitude
print(dir(rf))

# Ferme l'ODB
odb.close()