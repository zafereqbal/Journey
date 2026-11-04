class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Return an empty list if the input string is empty
        if not digits:
            return []
            
        # Map digits to their corresponding letters as on a phone keypad
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(index, current_combination):
            # Base case: if the current combination is of the same length as digits
            if len(current_combination) == len(digits):
                combinations.append("".join(current_combination))
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Explore each letter option
            for letter in letters:
                current_combination.append(letter)
                # Move to the next digit
                backtrack(index + 1, current_combination)
                # Backtrack to try the next letter
                current_combination.pop()
        
        # Initiate the backtracking process starting at index 0
        backtrack(0, [])
        return combinations
