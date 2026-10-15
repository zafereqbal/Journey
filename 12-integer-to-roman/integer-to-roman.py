class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Mapping of Roman numeral values in descending order
        roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        # Loop through each value-symbol pair
        for value, symbol in roman_mapping:
            # Determine how many times the current symbol fits into num
            if num >= value:
                count = num // value
                result.append(symbol * count)
                num %= value  # Update num with the remainder
                
        return "".join(result)
