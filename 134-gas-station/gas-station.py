class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < 0:
                start_index = i + 1
                total_tank = 0
        return start_index