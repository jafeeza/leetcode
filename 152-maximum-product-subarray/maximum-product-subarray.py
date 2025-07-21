class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmax,curmin=1,1
        for n in nums:
            if n==0:
                curmax,curmin=1,1
                continue
            temp=curmax
            curmax=max(n*curmax,n,n*curmin)
            curmin=min(n*temp,n,n*curmin)
            res=max(res,curmax)
        return res