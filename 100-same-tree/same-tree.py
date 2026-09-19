# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # 1. Both trees are empty
        if not p and not q:
            return True
        
        # 2. One tree is empty, and the other is not
        if not p or not q:
            return False
        
        # 3. The values of the current nodes are different
        if p.val != q.val:
            return False
        
        # 4. Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
