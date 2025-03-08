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
