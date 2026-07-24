class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        rows, cols = len(grid), len(grid[0])

        def helper(r, c):
            
            q = deque([[r,c]])
            directions = [(-1, 0), (1,0), (0,-1), (0,1)]
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r >= 0 and c >=0 and r < rows and c < cols and grid[r][c] == "1":
                        q.append([r,c])
                        grid[r][c] = "0"



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    helper(r , c)
                    res+=1
        return res
        