class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # color array: 0 means uncolored, 1 means Set A, -1 means Set B
        color = [0] * len(graph)
        
        # Loop through all nodes to handle disconnected components
        for i in range(len(graph)):
            if color[i] == 0:
                # Start BFS from this uncolored node
                queue = [i]
                color[i] = 1 # Assign initial color
                
                while queue:
                    node = queue.pop(0)
                    
                    for neighbor in graph[node]:
                        # If neighbor has the same color, it's not bipartite
                        if color[neighbor] == color[node]:
                            return False
                        
                        # If neighbor is uncolored, color it with the opposite color
                        if color[neighbor] == 0:
                            color[neighbor] = -color[node]
                            queue.append(neighbor)
                            
        return True
