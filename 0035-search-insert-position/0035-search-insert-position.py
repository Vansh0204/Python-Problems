class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = len(nums)  # default insert at the end
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break
            elif nums[i] > target:
                a = i
                break
        return a