'''Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1.
Input
User Task
This is a function problem. You don't have to take any input. You are required to complete the function minStartValue() which takes an array nums as parameter.

Custom Input
The first line contains a single integer n, representing the size of array nums.
The second line will take n space-separated integers representing elements of the nums array.

Constraints:
1 ≤ n ≤ 105
-103 ≤ nums[i] ≤ 103
Output
Return a single integer representing the minimum positive value of startValue such that the step by step sum is never less than 1.
Example
Input
5
-3 2 -3 4 2
Output
5
Explanation
If we choose, startValue = 5, the value of startValue after adding elements of array nums from left to right will be
(5 - 3) = 2
(2 + 2) = 4
(4 - 3) = 1
(1 + 4) = 5
(5 + 2) = 7
If you choose startValue = 4, in the third iteration your step by step sum is less than 1.'''
def minStartValue(nums):
    m= 0
    c= 0
    
    for num in nums:
        c+= num
        m = min(m, c)
    if m < 0: 
        return 1 - m 
    else:
        return 1
