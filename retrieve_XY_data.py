import abaqus
import abaqusConstants

print("sals")
odb = abaqus.session.openOdb(name= "combinaison_48.odb")

last_step = odb.steps.values()[-1]
last_frame = last_step.frames[-1]
print(last_frame.fieldOutputs)