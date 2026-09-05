class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = [root]
        index = 0

        while index < len(queue):
            level = []
            size = len(queue) - index

            for _ in range(size):
                node = queue[index]
                index += 1

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result