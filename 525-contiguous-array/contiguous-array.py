class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {0: -1}
        max_len = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_map:
                max_len = max(max_len, i - count_map[count])
            else:
                count_map[count] = i
        return max_len