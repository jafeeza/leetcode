class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ma=-1
        for i in range(0,n):
            for j in range(i+1,n):
                if i<j and nums[i]<nums[j]:
                    ma=max(ma,nums[j]-nums[i])
        return ma