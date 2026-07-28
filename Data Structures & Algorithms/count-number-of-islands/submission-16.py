class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def helper(r,c):
            directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
            q = deque([(r,c)])

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r,c = dr+row, dc+col
                    if r >=0 and c >=0 and r<ROWS and c < COLS and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    helper(r,c)
                    islands +=1

        return islands