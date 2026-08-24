class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        count = 0

        for i in range(n):
            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count