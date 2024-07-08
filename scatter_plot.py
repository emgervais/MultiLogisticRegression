import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys
from describe import getData
from histogram import sortHouse, findIndex

def plot(xIndex, yIndex, xLabel, YLabel, dataByHouse):
    house = [np.array(dataByHouse[0], dtype=object), 
             np.array(dataByHouse[1], dtype=object), 
             np.array(dataByHouse[2], dtype=object), 
             np.array(dataByHouse[3], dtype=object)]
    color = ['red', 'yellow', 'green', 'blue']
    i = 0

    plt.figure()
    plt.xlabel(xLabel)
    plt.ylabel(YLabel)
    for element in house:
        x = element[:, xIndex]
        y = element[:, yIndex]

        x = np.array([float(a) if a not in [None, ''] else np.nan for a in x], dtype=float)
        y = np.array([float(a) if a not in [None, ''] else np.nan for a in y], dtype=float)

        valid_mask = ~np.isnan(x) & ~np.isnan(y)

        x = x[valid_mask]
        y = y[valid_mask]

        plt.scatter(x, y, color=color[i], alpha=0.5)
        plt.title(f'House Grades')
        i += 1

def scatter_all_plot(dataByHouse, index, numerical):
    i = 0
    while i < len(numerical):
        j = 0
        indexX = findIndex(index, numerical[i][0])
        while j < len(numerical):
            if(j == i):
                j+=1
                continue
            indexY = findIndex(index, numerical[j][0])
            plot(indexX, indexY, numerical[i][0], numerical[j][0], dataByHouse)
            j += 1
        i += 1
    plt.show()

def scatter_one_plot(dataByHouse, index, houses_name):
    Xindex = findIndex(index, 'Defense Against the Dark Arts')
    Yindex = findIndex(index, 'Astronomy')
    plot(Xindex, Yindex, index[0][Xindex], index[0][Yindex], dataByHouse)
    plt.legend(houses_name)
    plt.show()

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    numerical, data = getData(sys.argv[1])
    dataByHouse, houses_name = sortHouse(data)
    # scatter_all_plot(dataByHouse, data, numerical)
    scatter_one_plot(dataByHouse, data, houses_name)


if __name__ == "__main__":
	main()