import numpy as np
import random as rd
import matplotlib.pyplot as plt
def sign(a):
	if a > 0:
		return 1
	else :
		return -1
x = []
w = np.array([ 0 , 0 , 0 , 0 , 0 ])
y = []
num = 0
f = open('hw1_6_train.dat' , 'r')
for line in f.readlines() :
	L = line.split()
	x.append([1] + [ float(i) for i in L[:-1]] )
	y.append( int(L[-1]) )
	num += 1
S = 0
co = 1
D = []
for rt in range(1126) :
	update = 0
	w.fill(0)
	rd.seed(rt)
	order = [i for i in range(num)]
	rd.shuffle(order)
	while True:
		fin = True
		for i in order:
			t = w.dot(np.array(x[i]))
			if sign(t) != y[i]:
				w = w + co*y[i]*np.array(x[i])
				fin = False
				update += 1
		if fin:
			break
	D.append(update)
	S += update
print(S/1126)
plt.xlabel('number of updates')
plt.ylabel('frequency of number')
plt.hist(D , bins = 30 , color = 'cyan')
plt.savefig('prob6.png')
f.close()
