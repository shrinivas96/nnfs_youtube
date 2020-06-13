import numpy as np

inputs = [1, 2, 3, 4]

weights = [[1, 2, 3, 4],
           [1, 2, 3, 4],
           [1, 2, 3, 4]]

bias = [1, 2, 3]
"""
the real multiplication is
| w11 w12 w13 w14 |   | x1 |   | b1 |   | y1 |
| w21 w22 w23 w24 | . | x2 | + | b2 | = | y2 |
| w31 w32 w33 w34 |   | x3 |   | b3 |   | y3 |
"""

print("The goal is to multiply the weights and the inputs and then add the bias: W.x + b")
print("This will be done in three ways. The final answer will be the same in each case.")
print("The first way shows how each element is multiplied.")
print("The second way does the same thing in a loop.")
print("The third way uses numpy dot function.")

out1 = [inputs[0]*weights[0][0] + inputs[1]*weights[0][1] + inputs[2]*weights[0][2] + inputs[3]*weights[0][3] + bias[0],
        inputs[0]*weights[1][0] + inputs[1]*weights[1][1] + inputs[2]*weights[1][2] + inputs[3]*weights[1][3] + bias[1],
        inputs[0]*weights[2][0] + inputs[1]*weights[2][1] + inputs[2]*weights[2][2] + inputs[3]*weights[2][3] + bias[2]]

out2 = []
for weight, b in zip(weights, bias):
    neuron_output = 0
    for w, x in zip(weight, inputs):
        neuron_output += w*x
    neuron_output += b
    out2.append(neuron_output)

out3 = np.dot(weights, inputs) + bias

print("1:", out1)
print("2:", out2)
print("3:", out3)
