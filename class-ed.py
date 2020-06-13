import numpy as np

np.random.seed(0)


class layer_dense:
    def __init__(self, n_inputs, n_outputs):
        self.weights = np.random.rand(n_outputs, n_inputs)
        self.biases = np.zeros((1, n_outputs))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights.T) + self.biases
        pass

