class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def robLine(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Don't rob the last house
        case1 = robLine(nums[:-1])

        # Case 2: Don't rob the first house
        case2 = robLine(nums[1:])

        return max(case1, case2)