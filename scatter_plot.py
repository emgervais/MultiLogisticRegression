import matplotlib.pyplot as plt
import numpy as np
import sys
from describe import getData

def plot(data, index, pl, x, y, s):
    color = ['red', 'yellow', 'green', 'blue']
    i = 0

    for i in range(len(index) - 1):
        housex = data[index[i]:index[i + 1] , x]
        housex = np.array(housex, dtype=np.float64)
        housey = data[index[i]:index[i + 1] , y]
        housey = np.array(housey, dtype=np.float64)
        pl.scatter(housex, housey, s, color=color[i], alpha=0.5)
        i += 1

def scatter_one_plot(data, houses, x, y, pl=plt, s=20):
    change_indices = np.where(houses[:-1] != houses[1:])[0] + 1
    change_indices = np.concatenate(([0], change_indices, [len(data)]))
    plot(data, change_indices, pl, x, y, s)

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    np.set_printoptions(threshold=np.inf)
    array = getData(sys.argv[1])
    array = array[1:]
    sorted_index = np.argsort(array[:, 0], axis=0)
    byHouse = array[sorted_index]
    plt.figure()
    scatter_one_plot(byHouse, byHouse[:, 0], 6, 8)
    plt.title(f'House Grades')
    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the dark Art")
    plt.legend(np.unique(byHouse[:, 0]))
    plt.show()


if __name__ == "__main__":
	main()