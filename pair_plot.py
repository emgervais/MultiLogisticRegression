import matplotlib.pyplot as plt
import numpy as np
import sys
from describe import getData
from scatter_plot import scatter_one_plot
from histogram import plot_histogram



def all_plot(data, names, houses):
    data = data[:, 5:]
    size = len(data.T)
    _, ax= plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.20, hspace=0.20)
    for y in range(0, size):
        for x in range(0, size):
            if(y == x):
                plot_histogram(data, houses, x, ax[y, x])
            else:
                scatter_one_plot(data, houses, x, y, ax[y, x], 1)
            
            if y == size - 1:
                ax[y, x].set_xlabel(names[x].replace(' ', '\n'))
            else:
                ax[y, x].tick_params(labelbottom=False)
            if x == 0:
                ax[y, x].set_ylabel(names[y].replace(' ', '\n'))
            else:
                ax[y, x].tick_params(labelleft=False)

            ax[y, x].spines['right'].set_visible(False)
            ax[y, x].spines['top'].set_visible(False)


def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    array = getData(sys.argv[1])
    names = array[:1, 5:][0]
    array = array[1:]
    sorted_index = np.argsort(array[:, 0], axis=0)
    byHouse = array[sorted_index]
    all_plot(byHouse, names, byHouse[:, 0])
    plt.legend(np.unique(byHouse[:,0]), loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


if __name__ == "__main__":
	main()