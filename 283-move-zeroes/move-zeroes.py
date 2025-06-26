class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(0,len(nums)):
            if nums[i]:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
        return nums