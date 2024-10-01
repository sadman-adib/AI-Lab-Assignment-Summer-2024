import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
data = pd.read_csv("diabetes.csv", header=None)  
X = data.iloc[:, :-1].values  # All columns except the last one
y = data.iloc[:, -1].values   # Last column is the target

# convert a column of ones to X for the intercept (a) term
Xo = np.column_stack((np.ones(X.shape[0]), X))

# y = a + b1x1 + b2x2 + b3x3 + ....... + bnxn 
# b = (X^T X)^(-1) X^T y
coff = np.linalg.inv(Xo.T @ Xo) @ Xo.T @ y

# Extract intercept (a) and slopes (b1, b2, ..., bn)
a = coff[0]  # Intercept
b = coff[1:] # Slopes for each feature

# Print the intercept and slopes
print(f"(a): {a}")
print(f"(b): {b}")

# Prediction function for multiple regressiona
def predict(X):
    return a + np.dot(X, b)

# Making predictions for the dataset
y_pred = predict(X)

mse = np.mean((y - y_pred) ** 2)
print(f"Mean Squared Error: {mse}")

# Plotting the predictions against the actual values
# plt.scatter(y, y_pred, color='blue')
# plt.plot([min(y), max(y)], [min(y_pred), max(y_pred)], color='red', linewidth=2)
# plt.xlabel("Actual y")
# plt.ylabel("Predicted y")
# plt.title("Actual vs Predicted for Multiple Linear Regression")
# plt.show()
