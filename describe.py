import sys
import math
spacing = 30
mean = []
count = []
columns = []
def getData(name):
    # name = 'datasets/test.csv'
    with open(name, 'r') as file:
        file_contents = file.read()
    parse(file_contents)

def removeColumn(index, array):
    for sub_array in array:
        sub_array.pop(index)

def sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def parse(content):
    lines = content.strip().split('\n')
    array = [line.split(',') for line in lines]
    i = 0
    while i < len(array[0]):
        empty_count = 0
        remove_column = False
        temp_array = [array[0][i]]
        for element in array[1:]:
            if not element[i]:
                empty_count += 1
            elif not isNum(element[i]):
                remove_column = True
                break
            else:
                temp_array.append(float(element[i]))
        if not remove_column and empty_count != len(array) - 1:
            columns.append(temp_array)
        i += 1

def printFeature(_):
    line = "".ljust(10)
    for feature in columns:
        line += feature[0].ljust(spacing)
        feature.pop(0)
        feature = sort(feature)
    return line


def isNum(element):
    try:
        float(element)
    except ValueError:
        return False
    return True

def printCount(line):
    for i in range(len(columns)):
        count.append(len(columns[i]))
        line += str(f"{count[i]:.6f}").ljust(spacing)
    return line

def printMean(line):
    for i in range(len(columns)):
        total = float(0)
        for element in columns[i]:
            total += element
        mean.append(total / count[i])
        line += str(f"{total / count[i]:.6f}").ljust(spacing)
    return line

def printStd(line):
    for i in range(len(columns)):
        total = float(0)
        for element in columns[i]:
            total += pow(mean[i] - element, 2)
        line += str(f"{math.sqrt(total / count[i]):.6f}").ljust(spacing)
    return line

def printMin(line):
    for i in range(len(columns)):
        mini = float("inf")
        for element in columns[i]:
            if(element < mini):
                mini = element
        line += str(f"{mini:.6f}").ljust(spacing)
    return line

def printQuarter(line):
    for i in range(len(columns)):
        index = 0.25 * (count[i] - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = columns[i][ri - 1]
        result = xri + rf * (columns[i][ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printHalf(line):
    for i in range(len(columns)):
        index = 0.50 * (count[i] - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = columns[i][ri - 1]
        result = xri + rf * (columns[i][ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printQuarterx3(line):
    for i in range(len(columns)):
        index = 0.75 * (count[i] - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = columns[i][ri - 1]
        result = xri + rf * (columns[i][ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printMax(line):
    for i in range(len(columns)):
        mini = float("-inf")
        for element in columns[i]:
            if(element > mini):
                mini = element
        line += str(f"{mini:.6f}").ljust(spacing)
    return line

def printData(data):
    describe = {
        'feature':  printFeature,
        'Count':    printCount,
        'Mean':     printMean,
        'Std':    printStd,
        'Min':    printMin,
        '25%':    printQuarter,
        '50%':    printHalf,
        '75%':    printQuarterx3,
        'Max':    printMax
    }
    for element in describe:
        line = describe[element](element.ljust(10))
        print(line)

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    dataset = sys.argv[1]
    getData(dataset)
    printData(columns)

if __name__ == "__main__":
	main()