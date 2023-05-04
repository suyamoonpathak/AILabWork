import numpy as np

# Define input data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Define weights and bias
w = np.array([0.5, 0.5])
b = -0.75

# Define activation function (step function)
def step_function(x):
    if x < 0:
        return 0
    else:
        return 1

# Define perceptron function
def perceptron(x, w, b):
    return step_function(np.dot(x, w) + b)

# Test the perceptron with input data
for i in range(len(X)):
    output = perceptron(X[i], w, b)
    print("Input: " + str(X[i]) + " Output: " + str(output))