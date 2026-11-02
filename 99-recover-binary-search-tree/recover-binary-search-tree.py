# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Identify the two swapped nodes
            if self.prev and self.prev.val > node.val:
                # First violation: 'first' is the previous larger node
                if not self.first:
                    self.first = self.prev
                # Second violation (or if adjacent): 'second' is the current smaller node
                self.second = node
            
            # Track the current node as previous for the next step
            self.prev = node
            
            # Traverse the right subtree
            inorder(node.right)
            
        # Run the in-order traversal to find the incorrect nodes
        inorder(root)
        
        # Swap the values of the two mismatched nodes to fix the tree
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
