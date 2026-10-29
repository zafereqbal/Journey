# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Include the current node in the path tracking
            current_path.append(node.val)
            current_sum += node.val
            
            # If it's a leaf node, check if the path matches the target sum
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(list(current_path))  # Append a copy of the path
            else:
                # Continue traversing left and right subtrees
                dfs(node.left, current_path, current_sum)
                dfs(node.right, current_path, current_sum)
            
            # Backtrack: remove the current node before returning up the call stack
            current_path.pop()

        dfs(root, [], 0)
        return result
