class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c, 0])
        res = 0
        while q:
            row, col, time = q.popleft()

            for dr, dc in directions:
                r,c = dr+row, dc+col
                if r>=0 and c>=0 and r< ROWS and c < COLS and grid[r][c] == 1:
                    q.append([r,c,time+1])
                    grid[r][c] = 2

            res = max(res, time)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return res