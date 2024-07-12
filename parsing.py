import numpy as np
import csv

def getData(name):
    with open(name, 'r') as file:
        file_contents = file.read()
    return parse(file_contents)

def arrayToFloat(array):
    converted_list = []
    for line in array:
        temp_list = []
        for element in line:
            value = element
            try:
                value = np.float64(value)
            except:
                if not value:
                    value = np.nan
            temp_list.append(value)
        converted_list.append(temp_list)

    return  np.array(converted_list)

def parse(content):
    lines = content.strip().split('\n')
    array = [line.split(',') for line in lines]
    array = arrayToFloat(array)
    array = np.delete(array, 0, axis=1)
    return array