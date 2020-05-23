import numpy as np
import random as rd
import matplotlib.pyplot as plt
def sign(a):
	if a > 0:
		return 1
	else :
		return -1
x1 = []
w = np.array([ 0 , 0 , 0 , 0 , 0 ])
y1 = []
num = 0
f1 = open('hw1_7_train.dat' , 'r')
for line in f1.readlines() :
	L = line.split()
	x1.append([1] + [ float(i) for i in L[:-1]] )
	y1.append( int(L[-1]) )
	num += 1
f2 = open('hw1_7_test.dat' , 'r')
x2 = []
y2 = []
n = 0
for line in f2.readlines():
	L = line.split()
	x2.append( [1] + [ float(i) for i in L[:-1]] )
	y2.append( int(L[-1] ))
	n += 1
S = 0
co = 1
err_rate = []
for rt in range(1126) :
	w.fill(0)
	rd.seed(rt)
	pocket = np.array([ 0 , 0 , 0 , 0 , 0])
	pocket_err = num+1
	order = [i for i in range(num)]
	rd.shuffle(order)
	update = 0
	while update < 100:
		for i in order:
			t = w.dot(np.array(x1[i]))
			if sign(t) != y1[i]:
				w = w + co*y1[i]*np.array(x1[i])
				update += 1
			if update >= 100:
				break
	e = 0
	for i in range(n) :
		t = w.dot(np.array(x2[i]))
		if sign(t) != y2[i]:
			e += 1
	err_rate.append(e/n)
	S += (e/n)
print(S/1126)
plt.xlabel('error rate')
plt.ylabel('frequency of error rate')
plt.hist(err_rate , bins = 30 , color = 'cyan')
plt.savefig('prob8.png')
f1.close()
f2.close()