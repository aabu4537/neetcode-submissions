class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        if not matrix:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(r, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for r in range(ROWS):
            for c in range(COLS//2):
                matrix[r][c], matrix[r][COLS-c-1] = matrix[r][COLS-c-1], matrix[r][c]
        