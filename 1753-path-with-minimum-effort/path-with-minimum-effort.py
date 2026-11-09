class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])
        
        # Helper function to check if a path exists with a given maximum effort
        def canReach(max_effort):
            # Using a list with a head pointer to simulate a queue without imports
            queue = [(0, 0)]
            head = 0
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            
            # 4 possible directional movements
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while head < len(queue):
                r, c = queue[head]
                head += 1
                
                # Reached the destination
                if r == rows - 1 and c == cols - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        # Check if the height difference is within the allowed effort
                        if abs(heights[nr][nc] - heights[r][c]) <= max_effort:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                            
            return False

        # Binary search range for minimum effort
        low = 0
        high = 1000000
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                ans = mid
                high = mid - 1  # Try to find a smaller maximum effort
            else:
                low = mid + 1   # Increase the allowed effort
                
        return ans
