class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            directions = [[1, 0] , [-1,0] , [0, 1], [0, -1]]

            while q:
                rows, cols = q.popleft()
                for dr, dc in directions:
                    r,c = dr+rows, dc+cols
                    if r>= 0 and c>=0 and r < ROWS and c < COLS and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "0"


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count +=1
        
        return count
                
        