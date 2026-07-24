class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        self.max_area = 0

        def helper(r, c):
            area = 1
            q = deque([[r,c]])
            directions = ((-1, 0), (1, 0), (0,1), (0,-1))

            while q:
                row, col = q.popleft()
                grid[row][col] = 0
                for dr, dc in directions:
                    r,c = dr+row, dc+col
                    if r>= 0 and c>=0 and r < rows and c < cols and grid[r][c] == 1:
                        area +=1
                        q.append([r,c])
                        grid[r][c] = 0
            
            self.max_area = max(self.max_area, area)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    helper(r,c)

        return self.max_area
        