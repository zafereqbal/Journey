class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            # Partition point for nums1
            partition1 = (low + high) // 2
            # Partition point for nums2
            partition2 = total_left - partition1
            
            # Edges of the partition in nums1
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            # Edges of the partition in nums2
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Odd total length: median is the maximum of the left partition
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # Even total length: median is average of middle two elements
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            
            # Too far right in nums1, move left
            elif max_left1 > min_right2:
                high = partition1 - 1
            # Too far left in nums1, move right
            else:
                low = partition1 + 1
                
        return 0.0
