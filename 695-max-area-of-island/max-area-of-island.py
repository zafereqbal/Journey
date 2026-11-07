class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or the cell is water (0), area contributed is 0
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            # Mark the current cell as visited by changing it to 0
            grid[r][c] = 0
            
            # Recursively find the area in all 4 directions and sum them up plus 1 for the current cell
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        # Traverse every cell in the grid
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # Update the maximum area found so far
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
