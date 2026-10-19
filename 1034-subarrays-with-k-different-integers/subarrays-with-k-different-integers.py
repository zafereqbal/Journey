class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(distinct_limit):
            if distinct_limit == 0:
                return 0
            count = 0
            l = 0
            freq = {}

            for r in range (len(nums)):
                freq[nums[r]] = freq.get(nums[r],0) + 1

                while len(freq) > distinct_limit:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count += (r - l + 1)
            return count
        return atMost(k) - atMost(k - 1)