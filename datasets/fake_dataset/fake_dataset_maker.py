import numpy as np

input_array = np.load("datasets/fake_dataset/design_of_doe_22-11.npy")

output_array = np.random.random((input_array.shape[0],2))

np.save("datasets/fake_dataset/fake_results_of_doe_22-11.npy", output_array)
print(output_array)