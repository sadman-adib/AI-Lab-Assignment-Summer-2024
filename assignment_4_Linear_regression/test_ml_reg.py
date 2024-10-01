import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("test.csv")

import numpy as np
X = np.array(data['x'])
y = np.array(data['y'])

def loss_function(m, c):
    y_prediction = m*X + c
    MSE = np.average((y-y_prediction)**2)
    return MSE

def prediction(m, c):
    return m*X + c

rng = np.random.default_rng()
m = rng.random()
c = rng.random()

alpha = 0.01

print(f"Training Starting... the value of m and c: {m} , {c}")

for i in range(100000):
    loss = loss_function(m,c)
    print(f"iteration -> {i+1} ##### loss: {loss}, m: {m}, c: {c}")

    # weight update
    y_prediction = prediction(m, c)
    updated_m = m + (np.average((y-y_prediction)*X)) * (2*alpha)
    updated_c = c + (np.average((y-y_prediction)*1)) * (2*alpha)

    if updated_m == m and updated_c == c:
        break

    m = updated_m
    c = updated_c





print(f"Training Finished, the value of m and c: {m} , {c}, Training Loss: {loss}")


# plt.scatter(X,y)
# plt.xlabel("X")
# plt.ylabel("y")

# x_random = np.arange(1, 10, 0.5)
# y_prediction = m*x_random + c
# plt.plot(x_random, y_prediction)

# plt.show()

