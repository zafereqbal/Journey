# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function returns the height of the tree if balanced, or -1 if unbalanced
        def check_height(node):
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
                
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
                
            # Otherwise, return the actual height of this subtree
            return 1 + max(left_height, right_height)
        
        return check_height(root) != -1
