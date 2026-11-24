class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # Pass 1: Mark transitions using temporary states
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # 1 means currently live; 2 means originally live (now dying)
                        if board[nr][nc] in (1, 2):
                            live_neighbors += 1

                # Rule 1 & 3: Live cell dies
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2
                # Rule 4: Dead cell becomes live
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = -1

        # Pass 2: Convert temporary states to final 0s and 1s
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == -1:
                    board[r][c] = 1
