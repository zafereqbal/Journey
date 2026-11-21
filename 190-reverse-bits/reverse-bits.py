class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result