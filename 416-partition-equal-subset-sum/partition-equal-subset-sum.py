class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        
        # An odd total sum cannot be split into two equal halves
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # dp[s] is True if a subset with sum 's' can be formed
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Traverse backwards to avoid reusing the same element
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
            # Early exit if target is already reached
            if dp[target]:
                return True
                
        return dp[target]
