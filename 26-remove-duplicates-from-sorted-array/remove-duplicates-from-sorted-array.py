class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        nums.sort()
        while i<len(nums):
            if nums[i-1]==nums[i]:
                nums.pop(i)
            else:
                i=i+1
        return len(nums)