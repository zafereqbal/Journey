# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0
        def get_depth(node):
            if not node:
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        get_depth(root)
        return self.max_diameter