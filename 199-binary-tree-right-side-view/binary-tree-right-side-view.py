# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        right_view = []
        queue = deque([root])
        
        # Standard Level-Order Traversal (BFS)
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # If it's the last element in the current level, add it to our result
                if i == level_length - 1:
                    right_view.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return right_view
