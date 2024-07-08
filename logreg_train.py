
import numpy as np
from sklearn.metrics import accuracy_score
from scipy import stats
import time
import sys
import csv
from describe import getData, calculateMean, calculateStd, calculateMax, calculateMin
from histogram import sortHouse, findIndex

def onlyNumerical(column):
    for i in range(len(column)):
        try:
            float(column[i])
        except ValueError:
            return False
        if(np.isnan(np.float64(column[i]))):
            column[i] = calculateMean(column)
    return True

def filter(array_2d):
    filtered_columns = [col for col in array_2d.T if onlyNumerical(col)]
    return np.array(filtered_columns).T

def normalize(column, min_val, max_val):
    return (column - min_val) / (max_val - min_val)

def standarize(X):
    for col in range(X.shape[1]):
        column = X[:, col]
        # print(column)
        min_val = calculateMin(column)
        max_val = calculateMax(column)
        mean_val = calculateMean(column)
        std_val = calculateStd(column)
        column = (column - mean_val) / std_val
        column = normalize(column, min_val, max_val)
        X[:, col] = column
    return X

def getY(array, houses_name):
    Y = []
    i = findIndex(array, 'Hogwarts House')
    for line in array[1:]:
        Y.append(findIndex([houses_name], line[i]))
    return Y

def one_hot(Y, num_classes):
    return np.eye(num_classes)[Y]

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def MultinomialLogisticRegression(X, Y, learning_rate, iterations, regularization_strength=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8):
    m, n = X.shape
    houses = len(np.unique(Y))
    y_one_hot = one_hot(Y, houses)
    prev_accuracy = 0
    limit = 100
    patience = 0

    weights = np.random.randn(n, houses) * np.sqrt(2.0 / n)# he initialization
    m_t = np.zeros((n, houses))
    v_t = np.zeros((n, houses))
    t = 0
    for i in range(iterations):
            t += 1
            linear_model = np.dot(X, weights)
            y_pred = softmax(linear_model)
            
            dw = (1 / m) * np.dot(X.T, (y_pred - y_one_hot)) + (regularization_strength / m) * weights #L2 regulation
            m_t = beta1 * m_t + (1 - beta1) * dw
            v_t = beta2 * v_t + (1 - beta2) * (dw ** 2)

            m_t_hat = m_t / (1 - beta1 ** t)
            v_t_hat = v_t / (1 - beta2 ** t)
            weights -= learning_rate * m_t_hat / (np.sqrt(v_t_hat) + epsilon)
            current_accuracy = accuracy_score(predict(X, weights), Y)
            print(current_accuracy)
            if(current_accuracy < prev_accuracy):
                patience += 1
            prev_accuracy = current_accuracy
            if patience >= limit:
                print(i)
                return weights
    return weights


def predict(X, weights):
    
    linear_model = np.dot(X, weights)
    y_pred = softmax(linear_model)
    return np.argmax(y_pred, axis=1)

def insertData(predictions, name):
     with open('houses.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Index','Hogwarts House'])
        for i in range(len(predictions)):
            csv_writer.writerow([i, name[predictions[i]]])


def anova_f_value(X, index):
    num_features = X.shape[1]
    p_values = []
    
    for i in range(num_features):
        feature = X[:, i]
        p_value = compute_anova_f_value(feature, index)
        p_values.append(p_value)
    
    return np.array(p_values)

def compute_anova_f_value(feature, index):
    groups = [feature[0:index[0]], feature[index[0] + 1:index[1]], feature[index[1] + 1:index[2]], feature[index[2] + 1:index[3]]]
    group_means = [calculateMean(group) for group in groups]
    overall_mean = calculateMean(feature)
    
    ssb = sum(len(group) * (mean - overall_mean)**2 for group, mean in zip(groups, group_means))
    ssw = sum(sum((x - mean)**2 for x in group) for group, mean in zip(groups, group_means))

    k = len(groups)
    n = sum(len(group) for group in groups)
    df_between = k - 1
    df_within = n - k
    
    msb = ssb / df_between
    msw = ssw / df_within
    
    F = msb / msw
    p_value = stats.f.sf(F, df_between, df_within)
    return p_value    

def CreatenewFeature(byHouse):
    new_features = []

    for i in range(len(byHouse[0])):
        for j in range(i + 1, len(byHouse[0])):
            new_feature = byHouse[:, i] * byHouse[:, j]
            new_features.append(new_feature)

    new_features = np.array(new_features).T

    return np.hstack((byHouse, new_features))
        
def	main():
    start_time = time.time()
    if(len(sys.argv) != 2):
        print("Enter database name")
        exit(1)
    np.set_printoptions(threshold=np.inf)
    dataset = sys.argv[1]
    _, array = getData(dataset)
    _, houses_name = sortHouse(array)
    Y = getY(array, houses_name)
    array = array[1:]
    # original_indices = np.arange(array.shape[0])
    # sorted_indices = np.argsort(array[:, 0])
    # byHouse = array[sorted_indices]
    # original_indices_sorted = original_indices[sorted_indices]
    # index = []
    # for name in houses_name:
    #     # Get indices where the group label matches
    #     group_indices = np.where(byHouse[:, 0] == name)[0]
    #     index.append(group_indices[-1])
    # index.sort()
    byHouse = np.array(filter(array), dtype=float)
    byHouse = standarize(byHouse)
    # byHouse = CreatenewFeature(byHouse)
    # anova_score = anova_f_value(byHouse, index)
    # features_to_keep = np.where(anova_score < 0.3)[0]
    X = byHouse#[:, features_to_keep]
    # X = X[np.argsort(original_indices_sorted)]
    print(f"Step 1 took {time.time() - start_time:.2f} seconds")
    weights= MultinomialLogisticRegression(X, Y, 0.75, 10000)
    print(f"Step 2 took {time.time() - start_time:.2f} seconds")
    predictions = predict(X, weights)
    insertData(predictions, houses_name)

if __name__ == "__main__":
	main()