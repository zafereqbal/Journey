# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Initialize a list to hold our global maximum. 
        # Using a list allows us to mutate it inside the helper function.
        max_sum = [float('-inf')]
        
        def gain_from_subtree(node):
            if not node:
                return 0
            
            # Recursively get the max path sum from left and right subtrees.
            # If the contribution is negative, we drop it by taking max with 0.
            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)
            
            # Price of a new path with the current node as the highest peak/hook
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum if the current path is better
            max_sum[0] = max(max_sum[0], current_path_sum)
            
            # For the parent node calls, return the maximum single path contribution
            return node.val + max(left_gain, right_gain)
        
        gain_from_subtree(root)
        return max_sum[0]
