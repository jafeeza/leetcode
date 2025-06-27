class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat=[[1]*n for _ in range(m)]
        for col in range(1,m):
            for row in range(1,n):
                mat[col][row]=mat[col-1][row]+mat[col][row-1]
        return mat[m-1][n-1]