class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1

        return s[start:end + 1]