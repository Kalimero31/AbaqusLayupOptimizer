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

for frame in step.frames:
    try:
        rf = frame.fieldOutputs['RF'].getSubset(region=odb.rootAssembly.nodeSets['ALL NODES']).values
        for value in rf:
            if value.nodeLabel == nodeID:
                print(frame.frameId, value.data)
    except KeyError:
        print('Pas de data')

# Ferme l'ODB
odb.close()