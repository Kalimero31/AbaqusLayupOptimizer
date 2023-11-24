from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import pandas as pd
import os


class NeuralNetwork:
    def __init__(self, input_dim, output_dim):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(64, input_dim=self.input_dim, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(self.output_dim, activation='linear'))
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model

    def train(self, X_train, Y_train, X_test, Y_test, epochs=50, batch_size=10):
        history = self.model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, Y_test))
        self._plot_training_history(history)


    def _plot_training_history(self, history):
        plt.figure(figsize=(12,6))
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'])
        plt.show()

    def evaluate(self, X_test, Y_test):
        loss = self.model.evaluate(X_test, Y_test)
        return loss

    def save(self, filepath):
        self.model.save(filepath)