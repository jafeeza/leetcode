class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1,len(triangle)):
            for col in range(row+1):
                s=math.inf
                if col>0:
                    s=triangle[row-1][col-1]
                if col<row:
                    s=min(s,triangle[row-1][col])
                triangle[row][col]+=s
        return min(triangle[-1])