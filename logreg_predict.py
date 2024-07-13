import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from logreg_train import predict, StandardScaler
import sys

def main():
    if len(sys.argv) != 3:
        print("Enter database and weights file")
        exit(1)
    np.set_printoptions(threshold=np.inf)
    df = pd.read_csv(sys.argv[1])
    df2 = pd.read_csv(sys.argv[2])
    df = df.fillna(method='ffill')
    X = np.array(df[['Defense Against the Dark Arts', 'Charms', 'Herbology', 'Divination', 'Muggle Studies']], dtype=float)
    X_val_std = StandardScaler(X)
    house = list(df2)[:4]
    w = df2.values
    pred = predict(w, X_val_std, house)
    f = open("houses.csv", 'w+')
    f.write('Index,Hogwarts House\n')
    for i in range(0, len(pred)):
        f.write(f'{i},{pred[i]}\n')

if __name__ == "__main__":
    main()