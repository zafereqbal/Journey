class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Base case: if there are 2 or fewer nodes, they are all MHT roots
        if n <= 2:
            return [i for i in range(n)]
        
        # Build the adjacency list representation of the graph
        adj = {i: set() for i in range(n)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        # Initialize the first layer of leaves
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        # Trim leaves level by level until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                # Get the only neighbor of the leaf node
                neighbor = adj[leaf].pop()
                # Remove the leaf from its neighbor's set
                adj[neighbor].remove(leaf)
                
                # If the neighbor becomes a leaf, add it to the next layer
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        # The remaining nodes are the roots of the MHTs
        return leaves
