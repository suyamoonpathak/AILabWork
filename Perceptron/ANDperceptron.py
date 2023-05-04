import numpy as np

# Define input data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Define weights and bias
w = np.array([0, 0])
b = 0

# Define activation function (step function)
def step_function(x):
    if x < 0:
        return 0
    else:
        return 1

# Define perceptron function
def perceptron(x, w, b):
    return step_function(np.dot(x, w) + b)

# Define training function
def train(X, w, b):
    converged = False
    while not converged:
        converged = True
        for i in range(len(X)):
            x = X[i]
            output = perceptron(x, w, b)
            if output == 0:
                w += x
                b += 1
                converged = False
            elif output == 1:
                continue
    return w, b

# Train the perceptron with input data
w, b = train(X, w, b)

# Test the perceptron with input data
for i in range(len(X)):
    output = perceptron(X[i], w, b)
    print("Input: " + str(X[i]) + " Output: " + str(output))