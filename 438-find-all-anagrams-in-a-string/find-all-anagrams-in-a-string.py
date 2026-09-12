class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # If the pattern is longer than the string, no anagram can exist
        if len(p) > len(s):
            return []
            
        p_count = {}
        s_count = {}
        
        # Initialize the frequency counters for string p and the first window of s
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            
        # If the first window matches, index 0 is our first result
        results = [0] if p_count == s_count else []
        
        # Slide the window across the rest of string s
        left = 0
        for right in range(len(p), len(s)):
            # Add the new character entering the window from the right
            s_count[s[right]] = s_count.get(s[right], 0) + 1
            
            # Remove or decrement the character leaving the window from the left
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
                
            left += 1
            
            # Compare the maps of the current window and target pattern
            if s_count == p_count:
                results.append(left)
                
        return results
