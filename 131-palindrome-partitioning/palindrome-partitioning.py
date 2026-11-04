class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        
        def is_palindrome(sub_str):
            return sub_str == sub_str[::-1]
            
        def backtrack(start, path):
            # Base case: if we reached the end of the string, add current path to results
            if start == len(s):
                result.append(list(path))
                return
            
            # Explore choices
            for end in range(start + 1, len(s) + 1):
                current_substring = s[start:end]
                
                # If current substring is a palindrome, proceed deeper
                if is_palindrome(current_substring):
                    path.append(current_substring)
                    backtrack(end, path)
                    path.pop() # Backtrack to explore other choices
                    
        backtrack(0, [])
        return result
