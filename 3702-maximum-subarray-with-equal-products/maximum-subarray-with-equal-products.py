import math

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        # Optional pruning upper bound
        total_lcm = 1
        for x in nums:
            total_lcm = lcm(total_lcm, x)
        max_prod = total_lcm * max(nums)

        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                prod *= nums[j]
                if prod > max_prod:
                    break
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                    
        return ans
