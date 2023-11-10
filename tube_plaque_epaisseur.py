# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
from odbAccess import *

import math
import numpy as np
import matplotlib.pyplot as plot
import subprocess
from scipy.optimize import minimize

#changer
my_model = '1_plaque_plane'
my_model = '3_tube'

my_part = 'plaque_plane'
my_part = 'tube'

my_material = 'composite'
my_step = 'load'

thickness = []
displacement = []
fobj_array = []
x0 = [1., 1., 1.]

#limites
cons=(  {'type': 'ineq','fun': lambda x: 2-abs(x[0])},
        {'type': 'ineq','fun': lambda x: 2-abs(x[1])},
        {'type': 'ineq','fun': lambda x: 2-abs(x[2])},
        {'type': 'ineq','fun': lambda x: x[0]},
        {'type': 'ineq','fun': lambda x: x[1]},
        {'type': 'ineq','fun': lambda x: x[2]}
      )

def function(x):
    k = 0
    with open("!thickness_0.txt", "a") as fid:
        fid.write("{}".format(x[0]))
        fid.write("\n")
    with open("!thickness_90.txt", "a") as fid:
        fid.write("{}".format(x[1]))
        fid.write("\n")
    with open("!thickness_45.txt", "a") as fid:
        fid.write("{}".format(x[2]))
        fid.write("\n")    
    if x[0] <= 0:
        if x[1] <= 0:
            if x[2]<= 0:
                fobj = 1000
                k = k+1 
    if k < 0.5:
        #change epaisseur
        layupOrientation = None
        p = mdb.models[my_model].parts[my_part]
        f = p.faces
        faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
        region1 = p.sets['Set-1']
        compositeLayup = mdb.models[my_model].parts[my_part].compositeLayups['CompositeLayup']
        compositeLayup.deletePlies()
        compositeLayup.suppress()
        if x[0] <= 0.1:
            compositeLayup.CompositePly(suppressed=True, plyName='Ply-1', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[0], orientationType=SPECIFY_ORIENT, orientationValue=0.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        else:
            compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1,material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[0], orientationType=SPECIFY_ORIENT, orientationValue=0.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        if x[1] <= 0.1:
            compositeLayup.CompositePly(suppressed=True, plyName='Ply-2', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[1], orientationType=SPECIFY_ORIENT, orientationValue=90.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        else:
            compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[1], orientationType=SPECIFY_ORIENT, orientationValue=90.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        if x[2] <= 0.1:
            compositeLayup.CompositePly(suppressed=True, plyName='Ply-3', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[2], orientationType=SPECIFY_ORIENT, orientationValue=45.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        else:
            compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[2], orientationType=SPECIFY_ORIENT, orientationValue=45.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        if x[2] <= 0.1:
            compositeLayup.CompositePly(suppressed=True, plyName='Ply-4', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[2], orientationType=SPECIFY_ORIENT, orientationValue=-45.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        else:
            compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region1, material=my_material, thicknessType=SPECIFY_THICKNESS, thickness=x[2], orientationType=SPECIFY_ORIENT, orientationValue=-45.0, additionalRotationType=ROTATION_NONE, additionalRotationField='', axis=AXIS_3, angle=0.0, numIntPoints=3)
        compositeLayup.resume()
        
        #submit job
        mdb.Job(name='Job-1', model=my_model, description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
        mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
        mdb.jobs['Job-1'].waitForCompletion()
        
        # odb analysis
        session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(sectionResults=USE_ENVELOPE)
        odb = openOdb("C:/TEMP/Job-1.odb", readOnly=True)
        steps = odb.steps
        step1 = steps[my_step]
        frames = step1.frames
        frame = frames[-1]
        fields = frame.fieldOutputs
        u = fields['U']
        values = u.values

        tmp = 0.
        for val in values:
            magnitude = val.magnitude
            tmp = magnitude if magnitude > tmp else tmp
        var2 = tmp
        displacement.append(tmp)
        with open("!U_magnitude_maxi.txt", "a") as fid:
            fid.write("{}".format(tmp))
            fid.write("\n")
        
        with open("!champ_U.txt", "a") as fid:
            
            fid.write("------------------------------------")
            fid.write("\n")
            for val in values:
                fid.write("{}".format(val.data))
                fid.write("\n")
        #####
        session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(sectionResults=USE_ENVELOPE)
        odb = openOdb("C:/TEMP/Job-1.odb", readOnly=True)
        steps = odb.steps
        step1 = steps[my_step]
        frames = step1.frames
        frame = frames[-1]
        fields = frame.fieldOutputs
        sth = fields['STH']
        values = sth.values
        tmp = 0.
        for val in values:
            th = val.data
            tmp = th if th > tmp else tmp
        var3 = tmp
        thickness.append(tmp)
        with open("!Thickness_maxi.txt", "a") as fid:
            fid.write("{}".format(tmp))
            fid.write("\n")
            
        session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(sectionResults=USE_ENVELOPE)
        odb = openOdb("C:/TEMP/Job-1.odb", readOnly=True)
        steps = odb.steps
        step1 = steps[my_step]
        frames = step1.frames
        frame = frames[-1]
        fields = frame.fieldOutputs
        sth = fields['STH']
        values = sth.values
        tmp = 0.
        for val in values:
            th = val.data
            tmp = th if th > tmp else tmp
        var3 = tmp
        thickness.append(tmp)
        with open("!Thickness_maxi.txt", "a") as fid:
            fid.write("{}".format(tmp))
            fid.write("\n")
        #fonction objective    
        #fobj = (var2*(10) + var3)
        #fobj = (var2*var3)
        fobj = var2*10/(6.913) + var3/4
        #fonction objective pour le tube:
        #fobj = (0.5)*(var2)*10/3.462 + (0.5)*(var3)/4
        with open("!fobj.txt", "a") as fid:
            fid.write("{}".format(fobj))
            fid.write("\n")
        fobj_array.append(fobj)
        
    return(fobj)



# for h0 in np.arange(0.2,1.2,0.2):
#     for h90 in np.arange(0.2,1.2,0.2):
#         for h45 in np.arange(0.2,1.2,0.2):
#             x = [h0,h90,h45]
#             function(x)

function([0.35, 0.9, 0.2])
# x1 = [1,1,1,1]
# x2 = [0.881, 0.9058, 0.9605, 0.9605]
# x3 = [0.5,0.5,0.5,0.5]

# function(x1)
# function(x2)
# function(x3)
              

# res = minimize(function,x0,method='COBYLA', constraints=cons)

#os.rename("C:/TEMP/abaqus/results.txt", "U:/AS/results.txt")

#plot.plot(thickness, displacement, color="red")
#plot.plot(thickness,thickness_tot, color="green")
#plot.plot(thickness,fobj_array, color="blue")


