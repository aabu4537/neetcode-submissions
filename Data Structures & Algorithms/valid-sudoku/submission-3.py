class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        count =[ [set() for i in range(9)] for i in range(3)]

        print(count)

        for r in range(9):
            for c in range(9):
                box = (r//3) * 3 + (c//3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in count[0][r] or board[r][c] in count[1][c] or board[r][c] in count[2][box]:
                    return False
                count[0][r].add(board[r][c])
                count[1][c].add(board[r][c])
                count[2][box].add(board[r][c])

        return True

        