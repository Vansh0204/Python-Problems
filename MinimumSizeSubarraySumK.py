'''You are given an array arr of size n, and an integer k. You have to find the minimum length of a subarray of arr with sum greater than or equal to k.

Note: A subarray of an array is defined as a sequence of consecutive elements of an array.
 
Input
User Task
This is a function problem. You don't have to take any input. You are required to complete the function minSubArray() which takes an array arr  and integer k as parameters.

Custom Input
The first line will take two space-separated integers representing n and k.
The second line will take n space-separated integers representing elements of the nums array.

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ k ≤ 109
Output
Return a single integer representing the minimum length of subarray of arr with sum greater than or equal to k If no such subarray exist return 0.
Example
Input
7 19
5 2 5 5 3 1 5
Output
5
Explanation
Subarray from index 3 to 7 is the subarray with minimum possible length whose subarray sum is greater than or equal to 19.
5+5+3+1+5=19'''
def minSubArray(arr, k):
    n = len(arr)
    left = 0
    sum_window = 0
    min_length = float('inf')

    for right in range(n):
        sum_window += arr[right]  

        while sum_window >= k: 
            min_length = min(min_length, right - left + 1)
            sum_window -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
