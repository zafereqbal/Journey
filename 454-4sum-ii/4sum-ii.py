class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sum_counts = {}
        
        # Store all possible sums of pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                pair_sum = a + b
                sum_counts[pair_sum] = sum_counts.get(pair_sum, 0) + 1
                
        count = 0
        
        # Look for the opposite sum in pairs from nums3 and nums4
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_counts:
                    count += sum_counts[target]
                    
        return count
