class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Create an n x n DP table initialized to 0
        dp = [[0] * n for _ in range(n)]
        
        # Iterate backwards for the start index i
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1  # A single character has palindrome length 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]
