class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        curr_sum = 0
        ans = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while left <= right and curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            
            ans += (right - left + 1)
            
        return ans  