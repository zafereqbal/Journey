# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # If the main tree is empty, subRoot cannot be a subtree
        if not root:
            return False
            
        # 1. Check if the current tree matches subRoot
        if self.isSameTree(root, subRoot):
            return True
            
        # 2. Otherwise, recursively check left and right children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        """
        Helper function to check if two trees are identical in structure and values.
        """
        # Both are null -> identical
        if not p and not q:
            return True
        # One is null and the other isn't -> not identical
        if not p or not q:
            return False
        # Values don't match -> not identical
        if p.val != q.val:
            return False
            
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
