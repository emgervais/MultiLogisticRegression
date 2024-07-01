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
    sort_array = list(sort_array.values())
    return sort_array

def plotData(array, numerical_columns, data):
    histo = [np.array(array[0], dtype=object), np.array(array[1], dtype=object), np.array(array[2], dtype=object), np.array(array[3], dtype=object)]
    color = ['red', 'yellow', 'green', 'blue']
    i = 0
    for house in histo:
        house = house[:, 15]
        house = np.array([float(x) if x not in [None, ''] else np.nan for x in house], dtype=float)
        house = house[~np.isnan(house)]
        plt.hist(house, color=color[i], alpha=0.5)
        i+=1

    plt.xlabel('grade')
    plt.ylabel('amount of students')
    plt.title('Histogram of homogeneous score distribution')
    plt.show()

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    dataset = sys.argv[1]
    numerical_columns, array = getData(dataset)
    byHouse = sortHouse(array)
    plotData(byHouse, numerical_columns, array)

if __name__ == "__main__":
	main()