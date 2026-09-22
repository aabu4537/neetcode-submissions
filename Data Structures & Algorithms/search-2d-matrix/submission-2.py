class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        length = ROWS*COLS
        l,r = 0, length-1

        while l <= r:
            mid = l + (r-l) //2
            val = matrix[mid//COLS][mid%COLS]
            if val < target:
                l = mid+1
            elif val > target:
                r = mid-1
            else:
                return True

        return False


        