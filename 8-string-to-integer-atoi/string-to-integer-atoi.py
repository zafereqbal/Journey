class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check for sign
        sign = 1
        i = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Read digits and convert to integer
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply the determined sign
        res *= sign
        
        # 4. Clamp the integer within the 32-bit signed range [-2^31, 2^31 - 1]
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
