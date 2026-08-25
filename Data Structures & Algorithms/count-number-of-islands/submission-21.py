class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [(-1, 0), (1,0), (0,-1), (0,1)]
        def helper(r,c):
            q = deque([(r,c)])
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = dr+row, dc + col
                    if new_r>= 0 and new_c >= 0 and new_r < ROWS and new_c < COLS and grid[new_r][new_c] == "1":
                        grid[new_r][new_c] = "0"
                        q.append([new_r,new_c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    helper(r,c)
                    islands+=1
        
        return islands
        
        