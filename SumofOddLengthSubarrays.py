'''Given an array of positive integers arr of size n. The power of an array is defined as sum of all elements in it. Calculate the sum of powers of all possible odd - length subarrays.

Note: A subarray is a contiguous subsequence of the array.
Input
User Task
This is a function problem. You don't have to take any input. You are required to complete the function sumOddLengthSubarrays() which takes an array arr as parameter.

Custom Input
The first line contains a single integer n, representing the size of array arr.
The second line will take n space-separated integers representing elements of the arr array.

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 103
Output
Return the sum of powers of all possible odd - length subarrays.
Example
Input
5
1 4 2 5 3
Output
58
Explanation
The odd- length subarrays of A and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1, 4, 2] = 7
[4, 2, 5] = 11
[2, 5, 3] = 10
[1, 4, 2, 5, 3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58'''

def sumOddLengthSubarrays(arr):
        n = len(arr)
        subarrays = []
        s=0
        for i in range(n):
            for j in range(i, n):
                subarrays.append(arr[i:j+1])
        for i in range(len(subarrays)):
            if len(subarrays[i])%2!=0:
                for j in range(len(subarrays[i])):
                    s+=subarrays[i][j]
        return s

# MORE OPTIMISED SOLUTION

def sumOddLengthSubarrays(arr):
    n = len(arr)
    total_sum = 0

    for i in range(n):
        count = ((i + 1) * (n - i) + 1) // 2  
        total_sum += arr[i] * count 

    return total_sum
