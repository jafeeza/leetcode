class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=[]
        r=[-1]*n
        for i in range(2*n-1,-1,-1):
            curr=nums[i%n]
            while s and s[-1]<=curr:
                s.pop()
            if i<n:
                r[i]=s[-1] if s else -1
            s.append(curr)
        return r