class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = min(m - 1, n - 1)
        total_steps = m + n - 2
        ans = 1
        for i in range(1, k + 1):
            ans = ans * (total_steps - i + 1) // i
        return ans 