import abaqus
import abaqusConstants
import matplotlib.pyplot as plt

USEFUL_ATTRIBUTES = {'U' : 'magnitude',
                     'STH' : 'data',
                     'HSNFCCRT': "data",
                     'HSNFTCRT': "data",
                     'HSNMTCRT': "data",
                     'HSNMCCRT': "data",}

def get_output_last_frame(odb):
    #print(odb.steps.values())
    last_step = odb.steps.values()[-1]
    last_frame = last_step.frames[-1]
    return(last_frame.fieldOutputs)
    
def get_available_fields(odb):
    field_output = get_output_last_frame(odb)
    return({field_output[i].description : i for i in field_output.keys()})

def get_field_data(odb, field_name):
    field_output = get_output_last_frame(odb)
    attribute = USEFUL_ATTRIBUTES[field_name]
    return([getattr(i, attribute) for i in field_output[field_name].values])
