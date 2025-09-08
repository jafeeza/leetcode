class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        h={}
        res=-1
        for i in nums:
            h[i]=h.get(i,0)+1
        for a,b in h.items():
            if b==1:
                res=max(res,a)
        return res
