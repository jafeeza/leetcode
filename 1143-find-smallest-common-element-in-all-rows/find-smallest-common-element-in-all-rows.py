class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n=len(mat)
        d=defaultdict(int)
        for row in mat:
            for i in range(len(mat[0])):
                d[row[i]]+=1
        for k,v in d.items():
            if v==n:
                return k
        return -1
        