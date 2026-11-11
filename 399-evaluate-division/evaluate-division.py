class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the graph using standard dictionaries
        graph = {}
        for (u, v), val in zip(equations, values):
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = float(val)
            graph[v][u] = 1.0 / val

        # Step 2: Define Depth-First Search (DFS) to find paths
        def dfs(start, end, visited):
            # If the current node matches the destination, ratio is 1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            # Explore neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor, end, visited)
                    if product != -1.0:
                        return weight * product
                        
            return -1.0

        # Step 3: Evaluate each query
        results = []
        for c, d in queries:
            # If either variable is completely missing from equations, it's invalid
            if c not in graph or d not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(c, d, set()))
                
        return results
