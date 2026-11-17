class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n+1)
        dp[0] = 0
        for target in range(1, n+1):
            s=1
            while s*s <= target:
                square = s*s
                dp[target] = min(dp[target], 1 + dp[target - square])
                s += 1
        return dp[n]