from tensorflow.keras.models import load_model
import numpy as np

# Nom du modèle 
filename = "neural-networks-pretrained/neural_network_11-23.keras"

# Chargement du modèle
model = load_model(filename)

# Données d'entrée
# sample_input = np.array([[45,0,90,60,45,45,0,0,0]])
sample_input = np.array([[90, 45, 45, 45,  0, 90, 45, 0, 90]])

# Utiliser le modèle pour faire une prédiction
prediction = model.predict(sample_input)

# Imprimer la prédiction
print('Prédiction du modèle:', prediction)
