class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        
        # Initialize distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(m)]
        queue = []
        
        # Multi-source BFS initialization: Add all 0s to the queue
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        # Use a pointer index to avoid O(N) list popping shifts
        head = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while head < len(queue):
            r, c = queue[head]
            head += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # If a shorter path to a 0 is found, update and push to queue
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))
                        
        return dist
