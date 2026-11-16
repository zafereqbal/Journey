class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Pad DP table with an extra row and column of 0s to avoid boundary checks
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if matrix[r - 1][c - 1] == '1':
                    dp[r][c] = min(
                        dp[r - 1][c],      # Top
                        dp[r][c - 1],      # Left
                        dp[r - 1][c - 1]   # Top-left diagonal
                    ) + 1
                    max_side = max(max_side, dp[r][c])
                    
        return max_side * max_side
