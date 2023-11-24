import numpy as np

input_array = np.load('datasets/800_simulations_22-11-23 (1 error)/design_of_doe_22-11.npy')

print(input_array[0])
print(input_array[10])
print(input_array[20])
print(input_array[30])
print(input_array[40])
print(input_array[50])

output_array = np.load('datasets/800_simulations_22-11-23 (1 error)/results_of_doe_22-11.npy')


np.random.shuffle(input_array)
print('----')
print(input_array[0])
print(input_array[10])
print(input_array[20])
print(input_array[30])
print(input_array[40])
print(input_array[50])

# np.random.shuffle(output_array)

np.save('datasets/800_simulations_shuffled_dataset/input.npy', input_array)
# np.save('datasets/800_simulations_shuffled_dataset/output.npy', output_array)