class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Base case: Out of bounds or not an 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Temporarily mark border-connected 'O' as 'E' (Escaped)
            board[r][c] = 'E'
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1: Traverse borders and run DFS to protect connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
            
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
            
        # Step 2: Update the board based on safe ('E') vs surrounded ('O') cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Flip surrounded cells
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # Restore boundary-connected cells
