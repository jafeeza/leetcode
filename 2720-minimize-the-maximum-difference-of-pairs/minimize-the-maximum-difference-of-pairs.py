class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n=len(nums)
        def validp(t):
            ind,cnt=0,0
            while ind<n-1:
                if nums[ind+1]-nums[ind]<=t:
                    ind+=1
                    cnt+=1
                ind+=1
            return cnt
        l,r=0,nums[-1]-nums[0]
        while l<r:
            mid=l+(r-l)//2
            if validp(mid)>=p:
                r=mid
            else:
                l=mid+1
        return l
