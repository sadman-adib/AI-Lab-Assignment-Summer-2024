import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
data = pd.read_csv("diabetes.csv", header=None)  
X = data.iloc[:, :-1].values  # X: This extracts all the columns except the last one
y = data.iloc[:, -1].values   # y: This extracts the last column

# Reshape y to be a 2D column vector for consistent operations
y = y.reshape(-1, 1)


rng = np.random.default_rng()
m = rng.random(size=(X.shape[1], 1))  # A random weight for each feature in X
c = rng.random()

alpha = 0.1 # Learning rate


def loss_function(m, c):
    y_prediction = np.dot(X, m) + c
    MSE = np.mean((y - y_prediction) ** 2)
    return MSE


def prediction(m, c):
    return np.dot(X, m) + c

print(f"Training Starting... the initial values of m and c: {m} , {c}")

# Training loop
for i in range(10):
    loss = loss_function(m, c)
    print(f"Iteration {i+1} ##### Loss: {loss}, m: {m.flatten()}, c: {c}")

    y_prediction = prediction(m, c)

    updated_m = m + (np.mean((y - y_prediction) * X, axis=0)).reshape(-1, 1) * (2 * alpha)
    updated_c = c + np.mean((y - y_prediction)) * (2 * alpha)
    
    if np.allclose(updated_m, m) and np.allclose(updated_c, c):
        break

    m = updated_m
    c = updated_c

print(f"Training Finished, final values of m: {m.flatten()}, c: {c}, Training Loss: {loss}")


# plt.scatter(X[:, 0], y)
# plt.xlabel("X (First feature)")
# plt.ylabel("y")
# x_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
# y_pred_line = m[0] * x_range + c  
# plt.plot(x_range, y_pred_line)

# plt.show()
