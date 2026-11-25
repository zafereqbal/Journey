class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 131313, 131319

        def has_unique(length):
            p1 = pow(BASE1, length, MOD1)
            p2 = pow(BASE2, length, MOD2)

            h1 = 0
            h2 = 0
            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2

            seen = set()
            duplicates = set()
            
            key = (h1 << 32) | h2
            seen.add(key)

            for i in range(length, n):
                out_val = nums[i - length]
                in_val = nums[i]

                h1 = (h1 * BASE1 + in_val - out_val * p1) % MOD1
                h2 = (h2 * BASE2 + in_val - out_val * p2) % MOD2

                key = (h1 << 32) | h2
                if key in seen:
                    duplicates.add(key)
                else:
                    seen.add(key)

            return len(seen) > len(duplicates)

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if has_unique(mid):
                high = mid
            else:
                low = mid + 1

        return low
