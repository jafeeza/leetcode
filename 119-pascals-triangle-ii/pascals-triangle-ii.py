class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[]
        for row_num in range(rowIndex+1):
            row=[None for _ in range(row_num+1)]
            row[0],row[-1]=1,1
            for j in range(1, len(row)-1):
                row[j]=triangle[row_num-1][j-1]+triangle[row_num-1][j]
            triangle.append(row)
        return triangle[rowIndex]