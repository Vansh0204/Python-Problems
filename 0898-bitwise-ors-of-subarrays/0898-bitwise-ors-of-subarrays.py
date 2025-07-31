class Solution(object):
    def subarrayBitwiseORs(self, arr):
        res = set()
        curr = set()
        
        for num in arr:
            curr = {num | prev for prev in curr} | {num}
            res |= curr
        
        return len(res)

        