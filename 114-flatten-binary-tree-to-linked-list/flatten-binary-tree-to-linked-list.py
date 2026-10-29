# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            # If a left child exists, we need to wire it into the right side
            if curr.left:
                # Find the rightmost node of the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Connect the original right subtree to the rightmost node of the left subtree
                prev.right = curr.right
                
                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None
            
            # Move on to the next node on the right side
            curr = curr.right
