class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted=list(sorted(nums))
        n=len(nums)
        for i in range(n):
            if nums_sorted[i]!=nums[i]:
                break
        for j in range(n-1,-1,-1):
            if nums_sorted[j]!=nums[j]:
                break
        if j>i:
            return j-i+1
        return 0