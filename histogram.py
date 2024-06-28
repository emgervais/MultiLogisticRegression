import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys
from describe import calculateCount, calculateMean, calculateStd, getData, sort

# houseMean = {'housename', mean}

# def findIndex(data, target):
#     for index, element in enumerate(data[0]):
#         if element == target:
#             return index
#     return None

# def sortHouse(array):
#     sort_array = {}
#     house_index = findIndex(array, 'Hogwarts House')
#     for line in array[1:]:
#         house_name = line[house_index]
#         if house_name not in sort_array:
#             sort_array[house_name] = []
#         sort_array[house_name].append(line)
#     return sort_array
            
# def calculateStdBySubject(sorted_by_house, index):
#     std = []
#     for value in sorted_by_house.values():
#         array = []
#         for element in value:
#             if(element[index]):
#                 array.append(float(element[index]))
#         std.append(calculateStd(array))
#     return calculateStd(std)
        

# def dataByHouse(array, numerical_columns):
#     sorted_by_house = sortHouse(array)
#     std_by_subject = {}
#     for column in numerical_columns:
#         index = findIndex(array, column[0])
#         std = calculateStdBySubject(sorted_by_house, index)
#         std_by_subject[column[0]] = float(0)
#         std_by_subject[column[0]] = std
#     return std_by_subject

def plotData(stds, subjects):
    sorted_data = sorted(zip(stds, subjects))
    stds, subjects = zip(*sorted_data)
    plt.bar(subjects, stds, align='center', alpha=0.5, ecolor='black', capsize=10)
    plt.ylabel('Scores')
    plt.title('Histogram with Standard Deviation by Subject')
    plt.show()

def stdByClass(data):
    std = []
    subjects = []
    # for column in data:
    for column in data[1:]:
        subarray = column[1:]
        std.append(calculateStd(subarray))
        subjects.append(column[0])
    return std, subjects

def reverseNormalize(arr):
    arr = np.array(arr)
    min_val = np.min(arr)
    max_val = np.max(arr)
    inverse_normalized_arr = 1 - (arr - min_val) / (max_val - min_val)
    return inverse_normalized_arr

def	main():
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    dataset = sys.argv[1]
    numerical_columns, _ = getData(dataset)
    stds, subjects = stdByClass(numerical_columns)
    stds = reverseNormalize(stds)
    plotData(stds, subjects)

if __name__ == "__main__":
	main()