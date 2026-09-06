"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # Handle the base case where the input graph is empty
        if not node:
            return None
        
        # Hash map to map original nodes to their corresponding cloned nodes
        old_to_new = {}
        
        # Recursive DFS helper function
        def dfs(curr_node):
            # If the node is already cloned, return its clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            # Create a clone for the current node (without neighbors initially)
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy
            
            # Recursively clone all the neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        # Start DFS traversal from the given starting node
        return dfs(node)