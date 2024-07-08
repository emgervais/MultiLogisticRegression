from sklearn.metrics import accuracy_score
import numpy as np

def getData():
    with open('houses.csv', 'r') as file:
        mine = file.read()
    with open('truth.csv', 'r') as file:
        real = file.read()
    return mine.split('\n'), real.split('\n')
    
def	main():
    mine, real = getData()
    print(accuracy_score(mine, real))


if __name__ == "__main__":
	main()