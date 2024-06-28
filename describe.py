import sys
import math
spacing = 30
def getData(name):
    # name = 'datasets/test.csv'
    with open(name, 'r') as file:
        file_contents = file.read()
    return parse(file_contents)

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
    removeColumn(0, array)
    numerical_columns = []
    for i in range(len(array[0])):
        empty_count = 0
        remove_column = False
        temp_array = [array[0][i]]
        for element in array[1:]:
            if not element[i]:
                empty_count += 1
            elif not isNum(element[i]):
                remove_column = True
            else:
                temp_array.append(float(element[i]))
        if not remove_column and empty_count != len(array) - 1:
            numerical_columns.append(temp_array)
    return numerical_columns, array



def isNum(element):
    try:
        float(element)
    except ValueError:
        return False
    return True

def printFeature(numerical_columns, _):
    line = "".ljust(10)
    for feature in numerical_columns:
        line += feature[0].ljust(spacing)
        feature.pop(0)
        feature = sort(feature)
    return line

def calculateCount(data):
    c = 0
    for element in data:
        if (element):
            c += 1
    return c

def printCount(numerical_columns, line):
    for data in numerical_columns:
        line += str(f"{calculateCount(data):.6f}").ljust(spacing)
    return line

def calculateMean(data):
    total = float(0)
    for element in data:
        if(element):
            total += element
    return total / calculateCount(data)

def printMean(numerical_columns, line):
    for data in numerical_columns:
        result = calculateMean(data)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def calculateStd(data):
    total = float(0)
    for element in data:
        if(element):
            total += pow(calculateMean(data) - element, 2)
    return math.sqrt(total / calculateCount(data))

def printStd(numerical_columns, line):
    for data in numerical_columns:
        line += str(f"{calculateStd(data):.6f}").ljust(spacing)
    return line

def printMin(numerical_columns, line):
    for i in range(len(numerical_columns)):
        mini = float("inf")
        for element in numerical_columns[i]:
            if(element < mini):
                mini = element
        line += str(f"{mini:.6f}").ljust(spacing)
    return line

def printQuarter(numerical_columns, line):
    for i in range(len(numerical_columns)):
        index = 0.25 * (calculateCount(numerical_columns[i]) - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = numerical_columns[i][ri - 1]
        result = xri + rf * (numerical_columns[i][ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printHalf(numerical_columns, line):
    for i in range(len(numerical_columns)):
        index = 0.50 * (calculateCount(numerical_columns[i]) - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = numerical_columns[i][ri - 1]
        result = xri + rf * (numerical_columns[i][ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printQuarterx3(numerical_columns, line):
    for i in range(len(numerical_columns)):
        index = 0.75 * (calculateCount(numerical_columns[i]) - 1) + 1
        ri = int(index)
        rf = index - ri
        xri = numerical_columns[i][ri - 1]
        result = xri + rf * (numerical_columns[i][ri] - xri)
        line += str(f"{result:.6f}").ljust(spacing)
    return line

def printMax(numerical_columns, line):
    for i in range(len(numerical_columns)):
        mini = float("-inf")
        for element in numerical_columns[i]:
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
        line = describe[element](data, element.ljust(10))
        print(line)

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    dataset = sys.argv[1]
    numerical_columns, _ = getData(dataset)
    printData(numerical_columns)

if __name__ == "__main__":
	main()