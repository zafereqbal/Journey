class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Stop at len(nums) - 1 because we don't need to jump once we reach the last index
        for i in range(len(nums) - 1):
            # Update the farthest index reachable from the current position
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump's range,
            # we must make another jump and update the new range end
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
