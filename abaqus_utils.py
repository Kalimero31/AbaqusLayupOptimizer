import abaqus
import abaqusConstants
import caeModules
import odbAccess

import os
import time
import math
import shutil

import numpy as np
import matplotlib.pyplot as plt

import objective_functions as objFuncs
import odb_field_extractor as odbFE

# del my_part.compositeLayups['CompositeLayup']

# Effectue la stratification a un composite layup
def make_stratification(composite_layup, region, material, 
                        layers):
    
    # On supprime les plis existants
    composite_layup.deletePlies()
    composite_layup.resume()
    
    # Itere sur la longueur de la liste des orientations
    for i in range(len(layers)):

        # Ajoute un pli avec epaisseur variable
        composite_layup.CompositePly(suppressed = False, 
                                    plyName = 'Ply-'+str(i+1), 
                                    region = region,
                                    material = material, 
                                    thicknessType = abaqusConstants.SPECIFY_THICKNESS, 
                                    thickness = 0.25, #mm
                                    orientationType = abaqusConstants.SPECIFY_ORIENT, 
                                    orientationValue = layers[i], 
                                    additionalRotationType = abaqusConstants.ROTATION_NONE, 
                                    additionalRotationField = '', 
                                    axis = abaqusConstants.AXIS_3, 
                                    angle = 0.0, 
                                    numIntPoints=3)
        
# Lance un job, gere les fichiers inutiles
def submit_job(job_name, model):
    # Creating the job
    abaqus.mdb.Job(name = job_name, 
                   model = model, 
                   description = '', 
                   type = abaqusConstants.ANALYSIS, 
                   atTime = None, 
                   waitMinutes = 0, 
                   waitHours = 0, 
                   queue = None, memory=90, 
                   memoryUnits = abaqusConstants.PERCENTAGE, 
                   getMemoryFromAnalysis = False, 
                   explicitPrecision = abaqusConstants.SINGLE, 
                   nodalOutputPrecision = abaqusConstants.SINGLE, 
                   echoPrint = abaqusConstants.OFF, 
                   modelPrint = abaqusConstants.OFF, 
                   contactPrint = abaqusConstants.OFF, 
                   historyPrint = abaqusConstants.OFF, 
                   userSubroutine = '', 
                   scratch = '', 
                   resultsFormat = abaqusConstants.ODB, 
                   multiprocessingMode = abaqusConstants.DEFAULT, 
                   numCpus = 1, 
                   numGPUs = 0)
    
    # Submitting the job
    abaqus.mdb.jobs[job_name].submit(consistencyChecking=abaqusConstants.OFF)

    # Waits the job is completed
    abaqus.mdb.jobs[job_name].waitForCompletion()
    time.sleep(1)

    # Moves .dat, .msg, .ipm, etc.. to the right folder
    move_data_file(job_name)

# Move les fichiers autres que .odb dans un dossier pour eviter superflu.
def move_data_file(job_name):
    files = [f for f in os.listdir(os.getcwd()) if f.startswith(job_name)]
    print(len(files))

    folder_name = job_name
    path_to_new_directory = os.path.join(os.getcwd(), folder_name)
    os.makedirs(path_to_new_directory)

    for i in files:
        if i!= job_name + '.odb':
            new_file_location = os.path.join(path_to_new_directory, os.path.basename(i))
            shutil.move(i, new_file_location)

# make_stratification(composite_layup, region, my_material,
#                     [0, 45, 90],
#                     [0.4, 0.2, 0.7]
#                     )


# k = 4
# submit_job('Job_test_vizu_' + str(k))

# my_odb = abaqus.session.openOdb(name='C:/temp/Job_test_vizu_' + str(k) +'.odb')
# abaqus.session.viewports['Viewport: 1'].setValues(displayedObject = my_odb)

# abaqus.session.viewports['Viewport: 1'].makeCurrent()
# abaqus.session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
#         abaqusConstants.CONTOURS_ON_DEF, ))
