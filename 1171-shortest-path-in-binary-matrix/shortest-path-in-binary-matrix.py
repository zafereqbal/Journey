class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # If the start or end cell is blocked, no path exists
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # Single-cell matrix edge case
        if n == 1:
            return 1
            
        # Initialize BFS queue with (row, col, current_distance)
        queue = [(0, 0, 1)]
        grid[0][0] = 1  # Mark the starting cell as visited
        head = 0        # Pointer to avoid using an expensive pop(0)
        
        # All 8 possible movement directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        while head < len(queue):
            r, c, dist = queue[head]
            head += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if the cell is unvisited (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    # Early exit condition when destination is reached
                    if nr == n - 1 and nc == n - 1:
                        return dist + 1
                        
                    grid[nr][nc] = 1  # Mark as visited
                    queue.append((nr, nc, dist + 1))
                    
        return -1
