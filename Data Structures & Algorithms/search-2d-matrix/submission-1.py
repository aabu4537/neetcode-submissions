class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix) , len(matrix[0])

        l,r = 0 , (m*n)-1

        while l <=r:
            m = (l+r)//2
            if matrix[m//n][m%n] > target:
                r = m -1
            elif matrix[m//n][m%n] < target:
                l = m +1
            else:
                return True

        return False
            
            
        