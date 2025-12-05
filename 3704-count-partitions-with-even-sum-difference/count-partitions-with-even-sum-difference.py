class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        p1,p2=0,0
        n=len(nums)
        c=0
        for i in range(0,n-1):
            p1=sum(nums[0:i+1])
            p2=sum(nums[i+1:n])
            if i==n-2:
                p2=nums[i+1]
            if abs(p1-p2)%2==0:
                c+=1
        return c