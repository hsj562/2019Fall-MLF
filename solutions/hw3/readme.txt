The implementation of Problem 7 and 8 are quite similar.
In Problem 7:

1. read the train data with function "readTrainData()" and store in x numpy array and y list

2. read the test data with function "readTestData()" and store them in xHat and yHat

3. gradient descent part is in function "gd()" and the w vector is named "w_gd". It trains 2000 times and for each time I used the formula that has taught in class to update w_gd and call the function "count_error()" to calculate the error rate for each iteration and append the result in "gd_Ein_list"

4. Finally, based on the result in "gd_Ein_list", plot a line chart with matplotlib.

5. The process of sgd is similar to gd but the only difference is that I used random number ( orderly from 1 to N ) replace the summation of N vectors. 	
