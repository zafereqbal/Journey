class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # The minimum capacity must be at least the heaviest package.
        # The maximum capacity would be the sum of all packages (shipping everything in 1 day).
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if the current capacity `mid` can ship everything within the allowed days
            current_weight = 0
            required_days = 1
            
            for weight in weights:
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0
                current_weight += weight
            
            # If it takes more days than allowed, the capacity is too small
            if required_days > days:
                left = mid + 1
            else:
                # If it's feasible, try to find a smaller working capacity
                right = mid
                
        return left
