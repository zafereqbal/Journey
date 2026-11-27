class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if there is only 1 row or the string is shorter than numRows,
        # no zigzag pattern is formed.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through each character and place it in the appropriate row
        for char in s:
            rows[current_row] += char
            
            # Reverse direction whenever we hit the top (0) or bottom (numRows - 1) row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move pointer up or down
            current_row += 1 if going_down else -1

        # Combine all rows into a single string
        return ''.join(rows)
