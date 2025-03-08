'''Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    min_val, max_val = min(nums), max(nums)
    if min_val == max_val:
        return 0  

    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1


    min_in_bucket = [float('inf')] * bucket_count
    max_in_bucket = [float('-inf')] * bucket_count
    has_element = [False] * bucket_count


    for num in nums:
        index = (num - min_val) // bucket_size
        min_in_bucket[index] = min(min_in_bucket[index], num)
        max_in_bucket[index] = max(max_in_bucket[index], num)
        has_element[index] = True

 
    prev_max = min_val
    max_gap = 0

    for i in range(bucket_count):
        if not has_element[i]:  
            continue
        max_gap = max(max_gap, min_in_bucket[i] - prev_max)
        prev_max = max_in_bucket[i]

    return max_gap


N = int(input().strip())
nums = list(map(int, input().split()))

print(maximumGap(nums))
