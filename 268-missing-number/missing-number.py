class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        c=0
        for i in nums:
            if c!=i:
                return c
            c+=1
        return c