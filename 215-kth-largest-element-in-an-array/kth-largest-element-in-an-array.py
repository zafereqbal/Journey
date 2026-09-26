class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        while nums:
            # Pick a pivot element from the middle to minimize worst-case behavior
            pivot = nums[len(nums) // 2]
            
            # 3-way partitioning
            left  = [x for x in nums if x > pivot]
            mid   = [x for x in nums if x == pivot]
            right = [x for x in nums if x < pivot]
            
            # Determine which partition contains the k-th largest element
            if len(left) >= k:
                nums = left
            elif len(left) + len(mid) >= k:
                return pivot
            else:
                k -= len(left) + len(mid)
                nums = right
