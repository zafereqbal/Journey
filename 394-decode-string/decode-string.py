class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Form the full multi-digit number k
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current accumulated string and number to the stack
                stack.append((current_string, current_num))
                # Reset tracking variables for the new nested context
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the last context from the stack
                prev_string, num = stack.pop()
                # Repeat the current decoded inner string and prepend the previous string context
                current_string = prev_string + (num * current_string)
            else:
                # Append standard letters to the current working string
                current_string += char
                
        return current_string
