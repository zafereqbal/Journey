class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # Pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # Maintain a monotonic increasing stack
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Calculate the area with the popped height
                max_area = max(max_area, height * (i - idx))
                # The current bar can extend backwards to the popped bar's index
                start = idx
            stack.append((start, h))
            
        # Clear out any remaining bars in the stack
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
            
        return max_area
