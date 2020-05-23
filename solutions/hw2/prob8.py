import random as rd
import numpy as np
import matplotlib.pyplot as plt
data_size = 2000
runtime = 1000
def sgn(x):
    if x > 0:
        return 1
    else :
        return -1
def gen_pair(data):
    for i in range(data_size):
        x = rd.uniform(-1,1)
        #print(x)
        p = rd.uniform(0,1)
        if x <= 0:
            y = -1
        else :
            y = 1
        if p < 0.2:
            y = -y
        data.update({x:y})
    return sorted(data)
data = {}
result = []
for r in range(runtime):
    data.clear()
    X = gen_pair(data)
    X_vector = np.array(X)
    h = [data[X[i]] for i in range(data_size)]
    h_vector = np.array(h)
    X.insert(0,-1)
    error_1 = 0
    error_2 = 0
    min_Ein = 2
    min_theta = 0
    sign = 0
    for i in range(data_size):
        mid = (X[i] + X[i+1])/2
        theta_vector = np.repeat(mid, data_size)
        result_pos = ( np.sign(X_vector-theta_vector) != h_vector)
        result_neg = ( np.sign(np.negative(X_vector - theta_vector)) != h_vector)
        error_1 = np.count_nonzero(result_pos)
        error_2 = np.count_nonzero(result_neg)
        m = min(error_1/data_size, error_2/data_size)
        if m < min_Ein:
            min_Ein = m
            min_theta = mid
            if error_1 < error_2:
                sign = 1
            else :
                sign = -1
    Eout = 0.5 - 0.3*sign*(1-abs(min_theta))
    result.append(min_Ein-Eout)
plt.xlabel('Ein-Eout')
plt.ylabel('frequency of number')
plt.hist(result, bins = 30, color = 'cyan')
plt.savefig('prob8.png')