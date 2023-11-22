# ====================================================================
# Entrainnement d'un réseau de neurone pour calculer les perturbations
# ====================================================================

import os 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import neural_network

# Creation du dataframe

input_array = np.load('C://temp/2020-1214/AbaqusLayupOptimizer/design_of_doe_mardi_2')
output_array = np.load('C://temp/2020-1214/AbaqusLayupOptimizer/results_of_doe_mardi_2')

# Choix des labels d'entrée et de sortie

X = input_array
Y = output_array

# Normalisation des données (Pour que tous les paramètres aient la même infuluence)
scaler = MinMaxScaler()

# X = scaler.fit_transform(X)
# Y = scaler.fit_transform(Y)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

# Création de l'objet NeuralNetwork
input_dim = X_train.shape[1]
output_dim = Y_train.shape[1]

neural_network = neural_network.NeuralNetwork(input_dim, output_dim)


# Entraînement du réseau de neurones
neural_network.train(X_train, Y_train, X_test, Y_test, epochs=200, batch_size=20)


# Affichage de la "perte" totale
loss = neural_network.evaluate(X_test, Y_test)

# Sauvegarde du modèle entrainé
neural_network.save('C://temp/2020-1214/AbaqusLayupOptimizer/PredictionModel_mardi.h5')

# Voir le fichier demo_use_neural_network.py pour l'utilisation d'un modèle enregistré.