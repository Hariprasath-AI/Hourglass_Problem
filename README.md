# Hourglass_Problem
Given a n * n 2D Array, arr:\
1 1 1 0 0 0\
0 1 0 0 0 0\
1 1 1 0 0 0\
0 0 0 0 0 0\
0 0 0 0 0 0\
0 0 0 0 0 0\
An hourglass in arr is a subset of values with indices falling in this pattern in 's graphical representation:\
a b c\
  d  \
e f g\
There are (n - 2) * (n - 2) hourglasses in arr. An hourglass sum is the sum of an hourglass' values.\
Calculate the hourglass sum for every hourglass in arr , then print the maximum hourglass sum. The array will always be n * n.

# Example
arr = \
-9 -9 -9  1 1 1\ 
 0 -9  0  4 3 2\
-9 -9 -9  1 2 3\
 0  0  8  6 6 0\
 0  0  0 -2 0 0\
 0  0  1  2 4 0\
The ((n - 2) * (n - 2)) hourglass sums are:
-63, -34, -9, 12,\ 
-10,   0, 28, 23,\
-27, -11, -2, 10,\ 
  9,  17, 25, 18\
The highest hourglass sum is  from the hourglass beginning at (1,1) and ends at (n-2,n-2) :
Here n is the length of row/column
0 4 3\
  1  \
8 6 6\
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Function Description

Complete the function hourglassSum in the editor below.\
hourglassSum has the following parameter(s):\
int arr[n][n]: an array of integers

# Returns

int: the maximum hourglass sum\

# Input Format

Each of the n lines of inputs arr[i] contains n space-separated integers arr[i][j].\

# Constraints
-9 <= arr[i][j] <= 9
0 <= i,j <= 5 

# Output Format
Print the largest (maximum) hourglass sum found in arr.

# Sample Input
1 1 1 0 0 0\
0 1 0 0 0 0\
1 1 1 0 0 0\
0 0 2 4 4 0\
0 0 0 2 0 0\
0 0 1 2 4 0

# Sample Output
19

# Explanation
arr contains the following hourglasses:
'''
1 1 1  1 1 0  1 0 0  0 0 0\
  1      0      0      0  \
1 1 1  1 1 0  1 0 0  0 0 0\
                          \
0 1 0  1 0 0  0 0 0  0 0 0\
  1      1      0      0  \
0 0 2  0 2 4  2 4 4  4 4 0\
                          \
1 1 1  1 1 0  1 0 0  0 0 0\
  0      2      4      4  \
0 0 0  0 0 2  0 2 0  2 0 0\
                          \
0 0 2  0 2 4  2 4 4  4 4 0\
  0      0      2      0  \
0 0 1  0 1 2  1 2 4  2 4 0\  
'''
