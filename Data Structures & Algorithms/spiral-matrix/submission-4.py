class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []
        
        ROWS, COLS = len(matrix), len(matrix[0])
        up, left =0, 0
        right, down = COLS-1, ROWS-1
        matrix_size = ROWS*COLS
        res = []
        while len(res) < matrix_size:
            #right
            for c in range(left, right+1):
                res.append(matrix[up][c])
            up += 1
            #down
            for r in range(up, down+1):
                res.append(matrix[r][right])
            right-=1
            #left
            if len(res) != matrix_size:
                for c in range(right, left-1, -1):
                    res.append(matrix[down][c])
                down-=1
            #up
            if len(res) != matrix_size:
                for r in range(down, up-1, -1):
                    res.append(matrix[r][left])
                left+=1
        return res


        