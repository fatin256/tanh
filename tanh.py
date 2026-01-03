import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

st.write("Tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))")

x = np.linspace(-10, 10, 400)
y = np.tanh(x)

plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.grid(True)

st.pyplot(plt)
