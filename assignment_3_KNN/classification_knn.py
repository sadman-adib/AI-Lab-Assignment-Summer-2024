import csv
import random
import numpy as np
from collections import Counter

with open('iris.csv', 'r') as file:
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

def knn_classification(dataset, train_set, K):
    correct_predictions = 0

    # dataset (either val_set or test_set)
    for V in dataset:
        L = []

        # Iterate over each sample in the training set
        for T in train_set:
            # Calculate the Euclidean distance between V and T (excluding the class label)
            distance = euclidean_distance(V[:-1], T[:-1])
            # Store T and the distance in list L
            L.append((T, distance))
        
        # Sort L by the distance in ascending order
        L.sort(key=lambda x: x[1])

        # Take the first K samples
        K_nearest = L[:K]

        # Determine the majority class from the knn
        K_classes = [sample[0][-1] for sample in K_nearest]
        detected_class = Counter(K_classes).most_common(1)[0][0]

        # Check if the detected class matches the true class
        if detected_class == V[-1]:
            correct_predictions += 1

    # Calculate accuracy
    accuracy = (correct_predictions / len(dataset)) * 100
    
    return accuracy


K = 15
val_accuracy = knn_classification(val_set, train_set, K)
print(f"Validation Accuracy: {val_accuracy:.2f}%")

test_accuracy = knn_classification(test_set, train_set, K)
print(f"Test Accuracy: {test_accuracy:.2f}%")