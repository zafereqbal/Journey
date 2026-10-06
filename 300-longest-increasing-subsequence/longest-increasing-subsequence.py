class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        # tails[i] stores the smallest tail of all increasing subsequences of length i+1
        tails = []
        
        for num in nums:
            # Manual binary search to find the correct insertion position
            low, high = 0, len(tails)
            while low < high:
                mid = (low + high) // 2
                if tails[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            
            # If num is larger than all elements, extend the sequence
            if low == len(tails):
                tails.append(num)
            # Otherwise, update the smallest tail at the found index
            else:
                tails[low] = num
                
        return len(tails)
