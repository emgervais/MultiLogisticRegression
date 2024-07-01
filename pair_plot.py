import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys
from describe import getData
from histogram import sortHouse, findIndex

def scatter(xIndex, yIndex, dataByHouse, ax):
    house = [np.array(dataByHouse[0], dtype=object), 
             np.array(dataByHouse[1], dtype=object), 
             np.array(dataByHouse[2], dtype=object), 
             np.array(dataByHouse[3], dtype=object)]
    color = ['red', 'yellow', 'green', 'blue']
    i = 0

    for element in house:
        x = element[:, xIndex]
        y = element[:, yIndex]

        x = np.array([float(a) if a not in [None, ''] else np.nan for a in x], dtype=float)
        y = np.array([float(a) if a not in [None, ''] else np.nan for a in y], dtype=float)

        valid_mask = ~np.isnan(x) & ~np.isnan(y)

        x = x[valid_mask]
        y = y[valid_mask]

        ax.scatter(x, y, s=1, color=color[i], alpha=0.5)
        i += 1

def histogram(xIndex, dataByHouse, ax):
    histo = [np.array(dataByHouse[0], dtype=object),
            np.array(dataByHouse[1], dtype=object), 
            np.array(dataByHouse[2], dtype=object), 
            np.array(dataByHouse[3], dtype=object)]
    color = ['red', 'yellow', 'green', 'blue']
    i = 0
    for house in histo:
        house = house[:, xIndex]
        house = np.array([float(x) if x not in [None, ''] else np.nan for x in house], dtype=float)
        house = house[~np.isnan(house)]
        ax.hist(house, color=color[i], alpha=0.5)
        i += 1

def all_plot(dataByHouse, index, numerical):
    size = len(numerical)
    _, ax= plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.20, hspace=0.20)
    for y in range(0, size):
        indexY = findIndex(index, numerical[y][0])
        for x in range(0, size):
            indexX = findIndex(index, numerical[x][0])
            if(y == x):
                histogram(indexX, dataByHouse, ax[y, x])
            else:
                scatter(indexX, indexY, dataByHouse, ax[y, x])
            
            if y == size - 1:
                ax[y, x].set_xlabel(numerical[x][0].replace(' ', '\n'))
            else:
                ax[y, x].tick_params(labelbottom=False)
            if x == 0:
                ax[y, x].set_ylabel(numerical[y][0].replace(' ', '\n'))
            else:
                ax[y, x].tick_params(labelleft=False)

            ax[y, x].spines['right'].set_visible(False)
            ax[y, x].spines['top'].set_visible(False)

    plt.show()


def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    numerical, data = getData(sys.argv[1])
    dataByHouse = sortHouse(data)
    all_plot(dataByHouse, data, numerical)


if __name__ == "__main__":
	main()