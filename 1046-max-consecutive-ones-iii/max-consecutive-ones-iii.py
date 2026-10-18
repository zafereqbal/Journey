class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If we find a 0, it consumes one allowed flip
            if nums[right] == 0:
                k -= 1
            
            # If we exceeded the allowed flips, shrink the window from the left
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
            # Update the maximum length of the valid window
            max_len = max(max_len, right - left + 1)
            
        return max_len
