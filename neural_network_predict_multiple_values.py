from tensorflow.keras.models import load_model
import numpy as np

# Nom du modèle 
filename = "neural-networks-pretrained/neural_network_11-23.keras"

# Chargement du modèle
model = load_model(filename)

# Données d'entrée
# sample_input = np.array([[45,0,90,60,45,45,0,0,0]])
sample_inputs = np.load('datasets/800_simulations_22-11-23 (1 error)/design_of_doe_22-11.npy')
sample_inputs_int32 = sample_inputs.astype(np.int32)

result = np.zeros((len(sample_inputs), 2))

for i in range(len(sample_inputs_int32)):
    i_batch = np.expand_dims(sample_inputs_int32[i], axis=0)
    prediction = model.predict(i_batch)
    result[i] = prediction

    # Imprimer la prédiction
    print('Prédiction du modèle:', prediction)

U = result[:,0]
hashin = result[:,1]

print(np.mean(U))
print(np.mean(hashin))

np.save("archives/test_datasets/result.npy", result)
np.save("archives/test_datasets/U.npy", U)
np.save("archives/test_datasets/hashin.npy", hashin)