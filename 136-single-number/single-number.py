class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        re=0
        l=len(nums)
        for i in range(1,len(nums),2):
            if nums[i]!=nums[i-1]:
                re=nums[i-1]
                return re
        re=nums[-1]
        return re