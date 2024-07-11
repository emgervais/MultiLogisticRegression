import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import time
import sys
import csv

def onlyNumerical(column):
    for i in range(len(column)):
        try:
            float(column[i])
        except ValueError:
            return False
        if(np.isnan(np.float64(column[i]))):
            column[i] = np.nanmean(column)
    return True

def filter(array_2d):
    filtered_columns = [col for col in array_2d.T if onlyNumerical(col)]
    return np.array(filtered_columns).T

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

def net_input(w, X):
    return sigmoid(w.dot(X.T))

def predict(w, X, houses):
    X = np.insert(X, 0, 1, axis=1)
    predictions = net_input(w, X).T
    return [houses[x] for x in predictions.argmax(1)]

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def main():
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Enter database name")
        exit(1)
    np.set_printoptions(threshold=np.inf)
    dataset = sys.argv[1]

    df = pd.read_csv(dataset)
    df = df.dropna(subset=['Defense Against the Dark Arts', 'Charms', 'Herbology', 'Divination', 'Muggle Studies'])
    
    X = np.array(df[['Defense Against the Dark Arts', 'Charms', 'Herbology', 'Divination', 'Muggle Studies']], dtype=float)
    y = df['Hogwarts House'].values

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25)

    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_val_std = sc.transform(X_val)

    eta = 0.01
    max_iter = 50
    Lambda = 10

    w = MultinomialLogisticRegression(X_train_std, y_train, eta, max_iter, Lambda)

    y_pred = predict(w, X_val_std, np.unique(y_train))
    print(f'Misclassified samples: {sum(y_val != y_pred)}')
    print(f'Accuracy: {accuracy_score(y_val, y_pred):.2f}')

    print(f"Total execution time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
