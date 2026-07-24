class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        q = deque()

        # 1. Find and mark initial border "O"s as safe ("T")
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and board[r][c] == "O":
                    q.append([r, c])
                    board[r][c] = "T" # Mark as temporarily safe

        directions = [(-1,0), (1,0), (0, 1), (0,-1)]
        
        # 2. Run BFS to turn all connected safe neighbors into "T"
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                    q.append([r, c])
                    board[r][c] = "T" # Mark neighbor as safe

        # 3. Final pass: Flip "O" to "X", and restore "T" to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X" # Trapped cells get flipped
                elif board[r][c] == "T":
                    board[r][c] = "O" # Safe cells get restored
