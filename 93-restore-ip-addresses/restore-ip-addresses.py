class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        def backtrack(start, path):
            # If we have exactly 4 segments and reached the end of the string, it's a valid IP
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Explore segments of length 1, 2, and 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                    
                segment = s[start:start+length]
                
                # Check for leading zeros: if length > 1, it cannot start with '0'
                if len(segment) > 1 and segment[0] == '0':
                    continue
                
                # Check value constraint: segment must be between 0 and 255
                if int(segment) <= 255:
                    backtrack(start + length, path + [segment])
                    
        backtrack(0, [])
        return res
