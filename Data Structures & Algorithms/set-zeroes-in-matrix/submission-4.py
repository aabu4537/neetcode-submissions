class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        # Check if the first row has any zeros
        row0_has_zero = False
        for c in range(COLS):
            if matrix[0][c] == 0:
                row0_has_zero = True
                break

        # Check if the first column has any zeros
        col0_has_zero = False
        for r in range(ROWS):
            if matrix[r][0] == 0:
                col0_has_zero = True
                break

        # Notice we start range at 1, not 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # Mark this row in our notebook
                    matrix[0][c] = 0  # Mark this col in our notebook

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if row0_has_zero:
            matrix[0] = [0] * COLS
            
        if col0_has_zero:
            for r in range(ROWS):
                matrix[r][0] = 0

                
                    
        

        
        