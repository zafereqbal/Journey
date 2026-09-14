class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            k = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                high = k
            else:
                low = k + 1

        return low