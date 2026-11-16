class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pad the array with 1 on both ends to handle out-of-bounds boundaries
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            # Base case: no balloons left between left and right boundaries
            if left + 1 >= right:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            max_coins = 0
            # Try every balloon 'i' between left and right as the LAST one to burst
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                coins += dfs(left, i) + dfs(i, right)
                max_coins = max(max_coins, coins)
                
            memo[(left, right)] = max_coins
            return max_coins

        return dfs(0, len(nums) - 1)
