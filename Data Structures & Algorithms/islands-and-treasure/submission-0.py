class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0,-1), (0,1)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c,0])
        

        while q:
            row, col, dist = q.popleft()

            for dr, dc in directions:
                r, c = dr+row, dc+col
                if r >=0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] == 2147483647:
                    q.append([r, c, dist+1])
                    grid[r][c] = dist+1

        return