import numpy as np
import math

def calculateCount(data):
    c = 0
    for element in data:
        if not np.isnan(element):
            c += 1
    return c

def calculateMean(data):
    total = 0
    for element in data:
        if not np.isnan(element):
            total += element
    return total / calculateCount(data)

def calculateStd(data):
    total = 0
    mean = calculateMean(data)
    for element in data:
        if not np.isnan(element):
            total += pow(mean - element, 2)
    return math.sqrt(total / calculateCount(data))

def calculateMax(column):
    mini = np.float64("-inf")
    for element in column:
        if(element > mini):
            mini = element
    return mini

def calculateMin(column):
    mini = np.float64("inf")
    for element in column:
        if(element < mini):
            mini = element
    return mini