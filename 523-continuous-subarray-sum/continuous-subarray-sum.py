class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_map = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k

            if rem in remainder_map:
                if i - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = i
        return False