# Affandka Febrian Putra Y
# 21091397030

import numpy as np

# Layer input 10 features
inputs = [1.3, 1.4, 1.5, 2.1, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
weights = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0]

# Neuron 1
bias = 3.2

outputs = np.dot(weights, inputs) + bias
print(outputs)