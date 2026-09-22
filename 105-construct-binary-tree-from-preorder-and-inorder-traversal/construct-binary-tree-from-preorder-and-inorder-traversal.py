# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map values to their indices in the inorder list for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Use an iterator over preorder to naturally get the root elements in sequence
        preorder_iter = iter(preorder)
        
        def helper(left_in_idx, right_in_idx):
            # Base case: no elements in this subtree
            if left_in_idx > right_in_idx:
                return None
            
            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find where this root splits the inorder list
            root_idx = inorder_map[root_val]
            
            # Always build the left subtree first because preorder is [Root -> Left -> Right]
            root.left = helper(left_in_idx, root_idx - 1)
            root.right = helper(root_idx + 1, right_in_idx)
            
            return root
            
        return helper(0, len(inorder) - 1)
