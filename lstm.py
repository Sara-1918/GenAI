# -*- coding: utf-8 -*-
"""LSTM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zrv9wYPfT6a9uhPu003eus0bWiBqAvNz
"""

import numpy as np
from tensorflow.keras.layers import LSTM,Dense
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt

sequence=np.array([i for i in range(1,101)])
sequence=np.array([i for i in range(1,101)])
window_size=3
x=[]
y=[]
for i in range(len(sequence)-window_size):
    x.append(sequence[i:i+window_size])
    y.append(sequence[i+window_size])
x=np.array(x)
y=np.array(y)

X=x.reshape(x.shape[0],x.shape[1],1)
model=Sequential()
model.add(LSTM(50,activation='relu',input_shape=(window_size,1)))
model.add(Dense(1))
model.compile(optimizer='adam',loss='mse')
model.fit(X,y,epochs=500,verbose=0)
print("Training complete")

import pickle

with open('/content/drive/MyDrive/GenAI/lstm_model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('/content/drive/MyDrive/GenAI/lstm_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

import gradio as gr

def predict_next(a, b, c):
    input_sequence = np.array([a, b, c])
    input_sequence = input_sequence.reshape((1, window_size, 1))
    prediction = model.predict(input_sequence)
    return f"Predicted next number: {prediction[0][0]:.2f}"

inputs = [gr.Number(label="Number 1"), gr.Number(label="Number 2"), gr.Number(label="Number 3")]
output = gr.Textbox(label="Output")

gr.Interface(fn=predict_next, inputs=inputs, outputs=output, title="Next Number Predictor with LSTM").launch()

predictions=model.predict(X)
plt.plot(y,label='True value')
plt.plot(predictions,label='Predicted value')
plt.legend()
plt.title('True value vs predicted value')
plt.show()

import gradio as gr

def predict_next(a, b, c):
    input_sequence = np.array([a, b, c])
    input_sequence = input_sequence.reshape((1, window_size, 1))
    prediction = model.predict(input_sequence)
    return f"Predicted next number: {prediction[0][0]:.2f}"

inputs = [gr.Number(label="Number 1"), gr.Number(label="Number 2"), gr.Number(label="Number 3")]
output = gr.Textbox(label="Output")

gr.Interface(fn=predict_next, inputs=inputs, outputs=output, title="Next Number Predictor with LSTM").launch()