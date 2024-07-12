import matplotlib.pyplot as plt
import sys
import numpy as np
from describe import getData

def findIndex(data, target):
    for index, element in enumerate(data[0]):
        if element == target:
            return index
    return None

def sortHouse(array):
    sort_array = {}
    house_index = findIndex(array, 'Hogwarts House')
    for line in array[1:]:
        house_name = line[house_index]
        if house_name not in sort_array:
            sort_array[house_name] = []
        sort_array[house_name].append(line)
    houses_name = list(sort_array.keys())
    sort_array = [np.array(value) for value in sort_array.values()]
    return sort_array, houses_name

def plot_histogram(array, houses, x, pl=plt):
    color = ['red', 'yellow', 'green', 'blue']
    change_indices = np.where(houses[:-1] != houses[1:])[0] + 1
    change_indices = np.concatenate(([0], change_indices, [len(array)]))
    for i in range(len(change_indices) - 1):
        house = array[change_indices[i]:change_indices[i + 1] , x]
        house = np.array(house, dtype=np.float64)
        pl.hist(house, color=color[i], alpha=0.5)


def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    array = getData(sys.argv[1])
    array = array[1:]
    sorted_index = np.argsort(array[:, 0], axis=0)
    byHouse = array[sorted_index]
    plot_histogram(byHouse, byHouse[:,0], 15)
    plt.xlabel('grade')
    plt.ylabel('amount of students')
    plt.title('Care of Magical Creatures')
    plt.legend(np.unique(array[:, 0]))
    plt.show()

if __name__ == "__main__":
	main()