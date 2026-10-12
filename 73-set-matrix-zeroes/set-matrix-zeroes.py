class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # 1. Check if the first row contains any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
                
        # 2. Check if the first column contains any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
                
        # 3. Use the first row and column as marker storage
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 4. Update the inner matrix based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 5. Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # 6. Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
