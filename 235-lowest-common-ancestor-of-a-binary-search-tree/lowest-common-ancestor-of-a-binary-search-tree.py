# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root
        
        while curr:
            # If both target nodes are greater, move to the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both target nodes are smaller, move to the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point (or found one of the nodes)
            else:
                return curr
