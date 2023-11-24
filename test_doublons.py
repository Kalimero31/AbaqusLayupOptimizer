import numpy as np

input_array = np.load('datasets/800_simulations_22-11-23 (1 error)/design_of_doe_22-11.npy')
output_array = np.load('datasets/800_simulations_22-11-23 (1 error)/results_of_doe_22-11.npy')

# input_array = np.array([[1,1], [1,1], [2,2], [2,3], [2,2], [4,2]])
# output_array = np.array([1,2,3,4,5,6])
print("input_array.shape", input_array.shape)


uniques, indexes ,counts = np.unique(input_array, axis=0, return_counts=True, return_index=True)

print("uniques", uniques)
print("counts", counts)
print("indexes", indexes)

print(np.unique(input_array[indexes], axis=0).shape)
print(output_array[indexes])
