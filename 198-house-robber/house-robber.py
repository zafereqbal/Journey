class Solution(object):
    def rob(self, nums):
        prev2 = 0
        prev1 = 0

        for money in nums:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1