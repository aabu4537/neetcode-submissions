class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])

        row_to_0 , col_to_0 = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_to_0[r] = True
                    col_to_0[c] = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if row_to_0[r] or col_to_0[c]:
                    matrix[r][c] = 0


                
                    
        

        
        