import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from maths import calculateMean, calculateStd
import time
import sys
import csv

def one_hot(Y, num_classes):
    label_map = {label: idx for idx, label in enumerate(sorted(set(Y)))}
    y_num = np.array([label_map[label] for label in Y])
    return np.eye(num_classes)[y_num]

def MultinomialLogisticRegression(X, y, eta=0.01, max_iter=500, Lambda=10):
    houses_num = len(np.unique(y))
    X = np.insert(X, 0, 1, axis=1)
    m, n = X.shape

    w = np.zeros((houses_num, n))
    yVec = one_hot(y, houses_num)

    for _ in range(max_iter):
        predictions = net_input(w, X).T
        dw = (1 / m) * (predictions - yVec).T.dot(X) + np.insert((Lambda / m) * w[:, 1:], 0, 0, axis=1)
        w -= eta * dw
    return w

def train_test_split(X, Y, test_size=0.20):
    p = np.random.permutation(len(X))   
    X_offset = int(len(X) * test_size)
    y_offset = int(len(Y) * test_size)  
    X_train = X[p][X_offset:]
    X_test = X[p][:X_offset]    
    y_train = Y[p][y_offset:]
    y_test = Y[p][:y_offset]
    return (X_train, X_test, y_train, y_test)

def net_input(w, X):
    return sigmoid(w.dot(X.T))

def predict(w, X, houses):
    X = np.insert(X, 0, 1, axis=1)
    predictions = net_input(w, X).T
    print(predictions)
    return [houses[x] for x in predictions.argmax(1)]

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def StandardScaler(X):
    mean = np.array([calculateMean(col) for col in X.T])
    std = np.array([calculateStd(col) for col in X.T])
    return (X - mean) / std

def insert_data(w, house):
    file = open("weights.csv", 'w+')
    for i in range(0, len(house)):
      file.write(f'{house[i]},')
    file.write("ok,ok")
    file.write('\n')
    for j in range(0, w.shape[0]):
        for i in range(0, w.shape[1]):
            file.write(f'{w[j][i]}')
            if i < w.shape[1] - 1:
                file.write(',')
        file.write('\n')

def main():
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Enter database name")
        exit(1)
    df = pd.read_csv(sys.argv[1])
    df = df.dropna(subset=['Defense Against the Dark Arts', 'Charms', 'Herbology', 'Divination', 'Muggle Studies'])
    
    X = np.array(df[['Defense Against the Dark Arts', 'Charms', 'Herbology', 'Divination', 'Muggle Studies']], dtype=float)
    y = df['Hogwarts House'].values

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25)

    X_train_std = StandardScaler(X_train)
    X_val_std = StandardScaler(X_val)

    eta = 0.01
    max_iter = 50
    Lambda = 10
    w = MultinomialLogisticRegression(X_train_std, y_train, eta, max_iter, Lambda)
    y_pred = predict(w, X_val_std, np.unique(y_train))
    print(f'Misclassified samples: {sum(y_val != y_pred)}')
    print(f'Accuracy: {accuracy_score(y_val, y_pred):.2f}')
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")
    insert_data(w, np.unique(y_train))

if __name__ == "__main__":
    main()
