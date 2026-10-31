class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        # Start with the root node
        leftmost = root
        
        # Loop down the levels of the tree
        while leftmost.left:
            # Iterate through the current level using the 'next' pointers
            head = leftmost
            while head:
                # Connection 1: Connect the two children of the same parent
                head.left.next = head.right
                
                # Connection 2: Connect the right child to the left child of the next parent
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node on the current level
                head = head.next
                
            # Move to the leftmost node of the next level
            leftmost = leftmost.left
            
        return root
