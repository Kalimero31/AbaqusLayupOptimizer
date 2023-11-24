# ====================================================================
# Entrainnement d'un réseau de neurone pour calculer les perturbations
# ====================================================================

import os
import datetime
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import lib.neural_network as neural_network


# Choix des labels d'entrée et de sortie

# X = np.load('datasets/800_simulations_22-11-23 (1 error)/design_of_doe_22-11.npy')
# Y = np.load('datasets/800_simulations_22-11-23 (1 error)/results_of_doe_22-11.npy')

X = np.load('datasets/fake_dataset/design_of_doe_22-11.npy')
Y = np.load('datasets/fake_dataset/fake_results_of_doe_22-11.npy')

# X = np.load('datasets/800_simulations_shuffled_dataset/input.npy')
# Y = np.load('datasets/800_simulations_shuffled_dataset/output.npy')


_, indexes = np.unique(X, axis=0, return_index=True)

X_uniques = X[indexes]
Y_uniques = Y[indexes]

print(X_uniques.shape)

print(np.unique(X_uniques, axis=0).shape)

# Normalisation des données (Pour que tous les paramètres aient la même infuluence)
# inutile ici car ils sont tous du même type
# scaler = MinMaxScaler()
# X = scaler.fit_transform(X)
# Y = scaler.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X_uniques, Y_uniques, test_size = 0.2)

# Création de l'objet NeuralNetwork
input_dim = X_train.shape[1]
output_dim = Y_train.shape[1]

neural_network = neural_network.NeuralNetwork(input_dim, output_dim)


# Entraînement du réseau de neurones
neural_network.train(X_train, Y_train, X_test, Y_test, epochs=5000, batch_size=40)


# Affichage de la "perte" totale
loss = neural_network.evaluate(X_test, Y_test)

# Sauvegarde du modèle entrainé
neural_network.save('neural-networks-pretrained/neural_network_' + 
                    datetime.datetime.now().strftime("%m-%d") + '.keras')

# Voir le fichier demo_use_neural_network.py pour l'utilisation d'un modèle enregistré.