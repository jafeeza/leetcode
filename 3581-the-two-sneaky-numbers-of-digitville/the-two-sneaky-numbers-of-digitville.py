class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        c={}
        for i in nums:
            c[i]= c.get(i,0)+1
            if c[i]==2:
                res.append(i)
        return res

        