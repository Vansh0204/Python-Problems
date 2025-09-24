class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        if sum(gas) < sum(cost):
            return -1
        current_tank = 0
        start=0
        for i in range(n-1):
            current_tank+=gas[i]-cost[i]
            if current_tank<0:
                start=i+1
                current_tank=0
        return start