import sys
import numpy as np
from parsing import getData
from maths import calculateCount, calculateMax, calculateMean, calculateMin, calculateStd

spacing = 30

def printFeature(data):
    line = "".ljust(10)
    for feature in data[0]:
        line += feature.ljust(spacing)
    print(line)

def printCount(data, line, _):

    for element in data.T:
        line += str(f"{calculateCount(element):.6f}").ljust(spacing)
    return line

def printMean(data, line, _):
    for column in data.T:
        result = calculateMean(column)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printStd(data, line, _):
    for column in data.T:
        line += str(f"{calculateStd(column):.6f}").ljust(spacing)
    return line

def printMin(data, line, _):
    for column in data.T:
        max = calculateMin(column)
        line += str(f"{max:.6f}").ljust(spacing)
    return line

def printPercent(data, line, percent):
    i = float(percent) / 100
    for column in data.T:
        column.sort()
        index = i * (calculateCount(column) - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = column[ri - 1]
        result = xri + rf * (column[ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printMax(data, line, _):
    for column in data.T:
        mini = calculateMax(column)
        line += str(f"{mini:.6f}").ljust(spacing)
    return line

def printData(data):
    describe = {
        'Count':    printCount,
        'Mean':     printMean,
        'Std':    printStd,
        'Min':    printMin,
        '25':    printPercent,
        '50':    printPercent,
        '75':    printPercent,
        'Max':    printMax
    }
    for element in describe:
        line = describe[element](data, element.ljust(10), element)
        print(line)

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    dataset = sys.argv[1]
    array = getData(dataset)
    printFeature(array[:1, 5:])
    array = np.array(array[1:, 5:], dtype=np.float64)
    printData(array)

if __name__ == "__main__":
	main()