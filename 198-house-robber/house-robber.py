class Solution:
    def rob(self, nums: List[int]) -> int:
        r1,r2=0,0 #[1,2,3,1]
        for n in nums: #[r1,r2]
            t=max(n+r1,r2) #[1,0] [2,1] [4,2] [3,4]
            r1=r2 #0 1 2 3
            r2=t #1 2 4 4
        return r2