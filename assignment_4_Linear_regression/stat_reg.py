import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  y=a+bx , a=y'-bx', y'=sum(y)/n, x'=sum(x)/n , b=sum(xi-x')(yi-y')/sum(xi-x')^2


data = pd.read_csv("test.csv")
X = np.array(data['x'])
y = np.array(data['y'])


x_mean = np.mean(X)
y_mean = np.mean(y)

b = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean) ** 2)

a = y_mean - b * x_mean


def prediction(X, a, b):
    return a + b * X

print(f"Values of a: {a}, b: {b}")


y_prediction = prediction(X, a, b)

# plt.scatter(X, y)
# plt.plot(X, y_prediction)
# plt.xlabel("X")
# plt.ylabel("y")
# plt.legend()
# plt.show()

MSE = np.mean((y - y_prediction) ** 2)
print(f"Training Loss (MSE): {MSE}")

