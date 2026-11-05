class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total_sum = sum(nums)
        # If the total sum cannot be divided into k equal parts, it's impossible
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        # Sort in descending order to optimize backtracking choices
        nums.sort(reverse=True)
        
        # If the largest number is greater than the target, no solution exists
        if nums[0] > target:
            return False
            
        memo = {}
        n = len(nums)
        
        def backtrack(mask, current_sum):
            # If all elements are used successfully
            if mask == (1 << n) - 1:
                return True
            
            # Return cached result if already computed
            if mask in memo:
                return memo[mask]
            
            for i in range(n):
                # Check if the i-th element is already taken
                if mask & (1 << i):
                    continue
                
                # If adding this element exceeds the target subset sum, skip it
                if current_sum + nums[i] > target:
                    continue
                
                # Transition to the next state
                next_mask = mask | (1 << i)
                next_sum = (current_sum + nums[i]) % target
                
                if backtrack(next_mask, next_sum):
                    memo[mask] = True
                    return True
            
            memo[mask] = False
            return False
            
        return backtrack(0, 0)
