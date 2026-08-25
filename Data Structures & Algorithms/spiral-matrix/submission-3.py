class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix:
            return []
        ROWS, COLS = len(matrix), len(matrix[0])
        right, down, left, up = 1,2,3,4 # directions
        top_b=  left_b = 0
        right_b, bottom_b = COLS-1, ROWS-1
        direction = right
        res = []  
        length_of_matrix = ROWS*COLS
        while len(res)< length_of_matrix:
            if direction == right:
                for c in range(left_b, right_b+1):
                    res.append(matrix[top_b][c])
                top_b+=1
                direction = down
            elif direction == down:
                for r in range(top_b, bottom_b+1):
                    res.append(matrix[r][right_b])
                right_b-=1
                direction = left
            elif direction == left:
                for c in range(right_b, left_b-1, -1):
                    res.append(matrix[bottom_b][c])
                bottom_b -= 1
                direction = up
            elif direction == up:
                for r in range(bottom_b, top_b-1, -1):
                    res.append(matrix[r][left_b])
                left_b+=1
                direction = right
        return res
                

    
