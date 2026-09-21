# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        
        while stack or curr:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the current node
            curr = stack.pop()
            k -= 1
            
            # If we've reached the kth element, return its value
            if k == 0:
                return curr.val
            
            # Move to the right subtree
            curr = curr.right
