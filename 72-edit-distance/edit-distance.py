class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # Create a (m + 1) x (n + 1) DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: transforming to/from an empty string
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Take the minimum of delete, insert, or replace
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # Delete
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j - 1]  # Replace
                    )
                    
        return dp[m][n]
