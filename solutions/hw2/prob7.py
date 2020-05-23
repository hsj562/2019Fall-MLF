import random as rd
import numpy as np
import matplotlib.pyplot as plt
data_size = 20
runtime = 1000
def sgn(x):
    if x > 0:
        return 1
    else :
        return -1
def gen_pair(data):
    for i in range(data_size):
        x = rd.uniform(-1,1)
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
    Ein_pos = []
    Ein_neg = []
    X.insert(0,-1)
    h = []
    for i in range(data_size):
        mid = (X[i] + X[i+1])/2
        h.append(mid)
        error_1 = 0
        error_2 = 0
        for x in X:
            if x == -1:
                continue
            if ( 1 * (sgn(x-mid)) ) != data[x]:
                error_1 += 1
            if ( -1 * (sgn(x-mid)) != data[x]) :
                error_2 += 1
        Ein_pos.append(error_1/data_size)
        Ein_neg.append(error_2/data_size)
    min_Ein = min(min(Ein_pos), min(Ein_neg))
    index = -1
    sign = 0
    for e in range(len(Ein_pos)):
        if Ein_pos[e] == min_Ein:
            index = e
            sign = 1 
            break
    if sign == 0:
        for e in range(len(Ein_neg)):
            if Ein_neg[e] == min_Ein:
                index = e
                sign = -1
                break
    theta = h[index]
    Eout = 0.5 - 0.3*sign*(1-abs(theta))
    result.append(min_Ein-Eout)
plt.xlabel('Ein-Eout')
plt.ylabel('frequency of number')
plt.hist(result, bins = 30, color = 'cyan')
plt.savefig('prob7.png')