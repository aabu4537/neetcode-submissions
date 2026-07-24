class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        def Helper(r,c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "$"
            
            found =   (Helper(r-1, c, i+1) or
                Helper(r+1, c, i+1) or
                Helper(r, c+1, i+1) or 
                Helper(r, c-1, i+1))
            
            board[r][c] = temp
            return found
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if Helper(r,c, 0): return True
        
        return False
                
        