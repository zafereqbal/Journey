class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case: if either number is "0", the product is always "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        # The result can have at most len(num1) + len(num2) digits
        result = [0] * (len(num1) + len(num2))
        
        # Reverse strings to process from right to left (least to most significant)
        num1, num2 = num1[::-1], num2[::-1]
        
        # Perform digit-by-digit multiplication
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Convert characters to single-digit integers using ASCII values
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Multiply the two digits and add to the current position
                product = digit1 * digit2
                result[i + j] += product
                
                # Handle the carry over to the next position
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
                
        # Remove any leading zeros (which are at the end of our reversed list)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
            
        # Reverse the array back to correct order and convert to string
        return "".join(str(digit) for digit in result[::-1])
