class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            current_num = nums[i % n]

            while stack and nums[stack[-1]] < current_num:
                pop_idx = stack.pop()
                res[pop_idx] = current_num
            if i < n :
                stack.append(i)
        return res