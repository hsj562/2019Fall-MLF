Discription:

Problem 7.
First of all, I generate the 20 data sets by the function gen_pair with random.uniform(). Then, because of 20% of the noise that flips the result, I randomly generate a number in [0,1] and if the number is smaller than 0.2, then I flip the yi to be -yi. Then, I chose every the median between every two xi and then use both positive ray and negative ray to calculate the error number with the given h(xi) and yi. Finally, choose the one with the minial errors divided by size to be our Ein. And the Eout is using the formula in problem 6, so we get Ein and Eout and we can calculate Ein - Eout.

Problem 8.
It is a little bit different from the method in Problem 7. Since I used the same method on this problem, I would get a long response time. Hence, I used the package numpy and transform those terms into vectors. Then, using the given form of h(x) to calculate a vector of h and we can compare vector of h and vector of y to get the error number with numpy.count_nonzero(). Hence, we can get the minimal Ein and using the formula in problem 6, so we get Eout as well.

Usage:

Problem 7.
    $python3 prob7.py

Problem 8.
    $python3 prob8.py
