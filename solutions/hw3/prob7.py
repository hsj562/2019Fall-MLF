import numpy as np
import math 
import random as rd
import matplotlib.pyplot as plt
N = 0
test_N = 0
r = 0
gd_Ein_list = []
#gd_Eout_list = []
sgd_Ein_list = []
#sgd_Eout_list = []
time_list = []
def readTrainData():
    global N
    x = []
    y = []
    f = open('hw3_train.dat', 'r')
    for line in f.readlines():
        L = line.split()
        x.append([1] + [ float(l) for l in L[:-1]] )
        y.append( int(L[-1]) )
        N += 1
    f.close()
    return np.array(x), y

def sigmoid(y_n, trans_w, x_n):
    s = -y_n * np.dot(trans_w, x_n)
    return 1.0/(1+math.exp(-s))

def gdEin(x,y,w):
    global N
    ret = np.array([0.0 for i in range(21)])
    for i in range(N):
        ret += sigmoid(y[i], w, x[i]) * (-y[i] * x[i])
    ret /= N
    return ret

def sgdEin(x,y,w):
    global r
    ret = np.array([0.0 for i in range(21)])
    ret += sigmoid(y[r], w, x[r]) * (-y[r] * x[r])
    r = (r + 1)%N
    return ret

def sgn(x):
    if x > 0:
        return 1
    else:
        return -1

def readTestData():
    global test_N
    x = []
    y = []
    f = open('hw3_test.dat', 'r')
    for line in f.readlines():
        L = line.split()
        x.append([1] + [float(l) for l in L[:-1] ])
        y.append(int(L[-1]) )
        test_N += 1
    f.close()
    return np.array(x), y

def count_err(w, xHat, yHat, n):
    cnt = 0
    for i in range(n):
        if(sgn(np.dot(w,xHat[i])) != yHat[i]):
            cnt += 1
    return float(cnt)/n

def gd(x, y, lr, tt, xHat, yHat): #normal gradient descent
    w_gd = np.array([ 0.0 for i in range(21)])
    for t in range(tt):
        w_gd = w_gd - lr * gdEin(x,y,w_gd)
        gd_Ein = count_err(w_gd, x, y, N)
        gd_Ein_list.append(gd_Ein)
        #gd_Eout = count_err(w_gd, xHat, yHat, test_N)
        #gd_Eout_list.append(gd_Eout)
        time_list.append(t+1)

def sgd(x, y, lr, tt, xHat, yHat): #stochastic gradient descent
    w_sgd = np.array([0.0 for i in range(21)])
    for t in range(tt):
        w_sgd = w_sgd - lr * sgdEin(x, y, w_sgd)
        sgd_Ein = count_err(w_sgd, x, y, N)
        sgd_Ein_list.append(sgd_Ein)
        #sgd_Eout = count_err(w_sgd, xHat, yHat, test_N)
        #sgd_Eout_list.append(sgd_Eout)
if __name__ == '__main__':
    training_time = 2000
    x,y = readTrainData()
    xHat,yHat = readTestData()
    gd(x, y, 0.01, training_time, xHat, yHat)
    sgd(x, y, 0.001, training_time, xHat, yHat)
    plt.xlabel('time stamp')
    plt.ylabel('Ein')
    plt.plot(time_list, gd_Ein_list, label = "gd")
    plt.plot(time_list, sgd_Ein_list, color = 'r', label="sgd")
    plt.savefig('prob7.png')