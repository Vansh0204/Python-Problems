'''You are given an odd integer N, representing the size of an N × N integer matrix Matrix, where Matrix[i][j] represents the element at the i-th row and j-th column.

Your task is to compute the sum of elements forming a plus pattern, consisting of:

Middle row.
Middle column.

Input
A single odd integer N representing the size of the matrix.
An N × N matrix consisting of integers.

Constraints
1 ≤ N ≤ 999 (N is always odd)
-104 <= matrix[i][j] <= 104

Output
A single integer representing the total sum of the specified plus-shaped elements.
Example:
Input
3
1 2 3
4 5 6
7 8 9

Output
25

Explanation
We can see that the sum of the middle row 4 5 6 and middle column 2 5 8 is (4 + 5 + 6) + (2 + 5 + 8)  - 5 = 25.'''
