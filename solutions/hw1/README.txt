Problem 6.
1. initialize "w" as zero vector and read the data from line to line
2. store components of vector in list "x" and the results in list "y" respectively
3. use the runtime(0~1125) as the seed of random and store the index in list "order" and then shuffle them
4. use a while loop to run the correction part and set a variable "fin" to record whether the process is finished or not and if there is any result that the sign of "w" dot "x[i]" is not equal to "y[i]", then we will correct "w" and let the number of update + 1
5. use variable S to sum up all the update time and if the 1126 times is finished then the average update time is S/1126
6. I used matplotlib to plot the histogram and save it as prob6.png file

Problem 7.
1. initialize "w" as zero vector
2. read the train data and store it in "x1" and "y1" and read the test data and store it in "x2" and "y2" separately
3. "err_rate" is an empty list use to record each error rate result
4. use the runtime(0~1125) as the seed of random and store the index in list "order" and then shuffle them
5. use train data to update "w", "pocket" is an array to store the current best "w" with the minimum errors and "pocket_err" is used to store the number of errors that "pocket" has
6. try 100 updates and during each updates, I check whether the "err" of the current "w" is less than "pocket_err", if it does, then I update the "pocket" to be current "w"
7. after 100 updates, I calculated the number of errors by dot "pocket" and "x2[i]" and if the sign of result is not equal to "y2[i]" then the number of errors "e" will be added by 1 
8. store "e/n" in the "err_rate" and use variable S to sum up all the "err_rate" and S/1126 is the average error rate
9. I used matplotlib to plot the histogram and save it as prob7.png file

Problem 8.
1. initialize "w" as zero vector
2. read the train data and store it in "x1" and "y1" and read the test data and store it in "x2" and "y2" separately
3. "err_rate" is an empty list use to record each error rate result
4. use the runtime(0~1125) as the seed of random and store the index in list "order" and then shuffle them
5. use train date to try 100 updates and use final "w" to check the test data by calculating the result of "w" dot "x2[i]" if the sign of the result is different from "y2[i]" then add "e" by 1
6. store "e/n" in the "err_rate" and use variable S to sum up all the "err_rate" and S/1126 is the average error rate
7. I used matplotlib to plot the histogram and save it as prob8.png file

