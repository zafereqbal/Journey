class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        # Accumulate sums for the first column
        for r in range(1, rows):
            grid[r][0] += grid[r - 1][0]

        # Accumulate sums for the first row
        for c in range(1, cols):
            grid[0][c] += grid[0][c - 1]

        # Compute minimum path sum for all remaining cells
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[-1][-1]
