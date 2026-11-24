class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # Step 1: Find up to two potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Step 2: Verify the candidates actually appear > n // 3 times
        result = []
        threshold = len(nums) // 3
        
        if nums.count(candidate1) > threshold:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > threshold:
            result.append(candidate2)
            
        return result
