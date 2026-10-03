class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        queue = []
        fresh_oranges = 0
        
        # Step 1: Initialize the queue with all initially rotten oranges 
        # and count the number of fresh oranges.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes have elapsed.
        if fresh_oranges == 0:
            return 0
            
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Step 2: Perform standard layer-by-layer Breadth-First Search (BFS)
        while queue and fresh_oranges > 0:
            minutes += 1
            next_queue = []
            
            for r, c in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if the neighboring cell is within bounds and contains a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Contaminate the orange
                        fresh_oranges -= 1
                        next_queue.append((nr, nc))
            
            queue = next_queue
            
        # Step 3: Return the result based on whether any fresh oranges remain
        return minutes if fresh_oranges == 0 else -1
