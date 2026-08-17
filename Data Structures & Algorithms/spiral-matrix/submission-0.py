class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []

        def spiral(rows, cols, r, c ,d_r, d_c):
            if rows == 0 or cols == 0:
                return
            
            for k in range(cols):
                r = r + d_r
                c = c + d_c
                res.append(matrix[r][c])
            
            # recursion
            spiral(cols, rows-1, r, c, d_c, -d_r)
        
        spiral(m, n, 0, -1, 0, 1)
        return res
            


            

        