import numpy as np
import pandas as pd


input_array = np.load("data/fake_dataset/design_of_doe_22-11.npy")
output_array = np.load("data/fake_dataset/fake_results_of_doe_22-11.npy")

# input_array = np.load("data/800_simulations_22-11-23 (1 error)/design_of_doe_22-11.npy")
# output_array = np.load("data/800_simulations_22-11-23 (1 error)/results_of_doe_22-11.npy")

# input_array = np.load("data/800_simulations_shuffled_dataset/input.npy")
# output_array = np.load("data/800_simulations_shuffled_dataset/output.npy")

# print(input_array.shape)
# print(output_array.shape)

dic_df = {"l1": input_array[:,0],
          "l2": input_array[:,1],
          "l3": input_array[:,2],
          "l4": input_array[:,3],
          "l5": input_array[:,4],
          "l6": input_array[:,5],
          "l7": input_array[:,6],
          "l8": input_array[:,7],
          "l9": input_array[:,8],
          "u": output_array[:,0],
          "hashin": output_array[:,1],
          }

df = pd.DataFrame(dic_df)

df.to_csv("data/random_dataset.csv")
print(df.head())