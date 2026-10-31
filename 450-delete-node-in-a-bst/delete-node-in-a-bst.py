# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # Base case: if the tree is empty
        if not root:
            return None
        
        # 1. Search for the node to remove
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Node found! Handle deletion cases:
            
            # Case 1: No left child (covers leaf node and right-only child cases)
            if not root.left:
                return root.right
            
            # Case 2: No right child (covers left-only child case)
            elif not root.right:
                return root.left
            
            # Case 3: Two children
            # Find the inorder successor (smallest value in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace current node's value with successor's value
            root.val = successor.val
            
            # Recursively delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root
