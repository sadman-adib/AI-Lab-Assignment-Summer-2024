import csv
import random
import numpy as np

with open('diabetes.csv', 'r') as file:
    reader = csv.reader(file)
    data_list = list(reader)

for i in range(0,len(data_list)):
    for j in range(0,len(data_list[i])):
        data_list[i][j] = float(data_list[i][j])

# count = 1
# for i in range(0, len(data_list)):
#     print(f"{count}. {data_list[i]}")
#     count += 1

train_set = []
val_set = []
test_set = []

# Shuffle the dataset
random.shuffle(data_list)

# Split the dataset
for sample in data_list:
    R = random.random()
    if 0 <= R <= 0.7:
        train_set.append(sample)
    elif 0.7 < R <= 0.85:
        val_set.append(sample)
    else:
        test_set.append(sample)

print(f"Training set size: {len(train_set)}")
print(f"Validation set size: {len(val_set)}")
print(f"Test set size: {len(test_set)}")



def euclidean_distance(sample1, sample2):
    return np.sqrt(np.sum((np.array(sample1) - np.array(sample2)) ** 2))

def knn_regression(dataset, train_set, K):
    Error = 0

    # dataset (either val_set or test_set)
    for V in dataset:
        L = []

        # Iterate over each sample in the training set
        for T in train_set:
            # Calculate the Euclidean distance between V and T (excluding the output value)
            distance = euclidean_distance(V[:-1], T[:-1])
            # Store T and the distance in list L
            L.append((T, distance))
        
        # Sort L by the distance in ascending order
        L.sort(key=lambda x: x[1])

        # Take the first K samples
        K_nearest = L[:K]

        # Calculate the average output of the K nearest samples
        determined_output = np.mean([sample[0][-1] for sample in K_nearest])

        # Calculate the squared error for this sample
        Error += (V[-1] - determined_output) ** 2

    # Calculate Mean Squared Error
    Mean_Squared_Error = Error / len(dataset)
    
    return Mean_Squared_Error


K = 20
val_mse = knn_regression(val_set, train_set, K)
print(f"Mean Squared Error on Validation Set: {val_mse}")

test_mse = knn_regression(test_set, train_set, K)
print(f"Mean Squared Error on Test Set: {test_mse}")

