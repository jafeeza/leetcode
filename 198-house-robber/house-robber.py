class Solution:
    def rob(self, nums: List[int]) -> int:
        r1,r2=0,0
        for n in nums:
            t=max(n+r1,r2)
            r1=r2
            r2=t
        return r2