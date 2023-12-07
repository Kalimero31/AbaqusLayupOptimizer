import abaqus
import abaqusConstants

odb = abaqus.session.openOdb(name= "combinaison_48.odb")

# last_step = odb.steps.values()[-1]
# last_frame = last_step.frames[-1]
# print(last_frame.fieldOutputs)

# Nom de la step
nom_step = 'load'  # Remplace par le nom de ta step

# ID du nœud pour lequel tu veux les RF
nodeID = 5

# Accède à la step
step = odb.steps[nom_step]

# Parcours tous les frames de la step
for frame in step.frames:
    # Extrait les RF pour le nœud spécifié
    try:
        rf = frame.fieldOutputs['RF'].getSubset(region=odb.rootAssembly.nodeSets['ALL NODES']).values
        for value in rf:
            if value.nodeLabel == nodeID:
                print(f'Frame {frame.frameId}: RF = {value.data}')
    except KeyError:
        print(f'Frame {frame.frameId}: Pas de données RF disponibles')

# Ferme l'ODB
odb.close()