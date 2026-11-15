from bisect import bisect_left

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort by width ascending, then height descending for equal widths
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        dp = []
        for _, h in envelopes:
            idx = bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
                
        return len(dp)
