class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        
        # Check if a valid subset sum is possible
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
            
        subset_sum = (total_sum + target) // 2
        
        # dp[j] stores the number of ways to achieve sum j
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # Base case: 1 way to make sum 0 (empty subset)
        
        for num in nums:
            # Iterate backwards to avoid reusing the same element multiple times
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_sum]
