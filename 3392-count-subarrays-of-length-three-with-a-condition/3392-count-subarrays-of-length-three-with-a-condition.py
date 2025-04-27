class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]
            if middle % 2 == 0:  # Middle must be evenly divisible by 2
                if (first + third) == (middle // 2):
                    count += 1
        return count