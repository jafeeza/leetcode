class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        if m==0:
            return false
        n=len(matrix[0])
        left,right=0,m*n-1
        while left<=right:
            mid=(left+right)//2
            pivot=matrix[mid//n][mid%n]
            if target==pivot:
                return True
            elif pivot>target:
                right=mid-1
            else:
                left=mid+1
        return False