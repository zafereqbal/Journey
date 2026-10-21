class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(max_sum):
            # Track current subarray count and current cumulative sum
            subarrays = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > max_sum:
                    # Start a new subarray
                    subarrays += 1
                    current_sum = num
                    # If we need more than k subarrays, max_sum is too small
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        # Binary search range
        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            if canSplit(mid):
                ans = mid       # mid is a valid largest sum, record it
                high = mid - 1  # try to find a smaller maximum sum
            else:
                low = mid + 1   # mid is too small, increase the allowed sum
                
        return ans
