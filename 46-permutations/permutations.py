class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start):
            # If we reached the end of the array, add the current permutation
            if start == len(nums):
                res.append(list(nums))
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the element at the index 'start'
                nums[start], nums[i] = nums[i], nums[start]
                
                # Move to the next index
                backtrack(start + 1)
                
                # Swap back to backtrack
                nums[start], nums[i] = nums[i], nums[start]
                
        backtrack(0)
        return res
