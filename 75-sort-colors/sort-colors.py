class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes,ones,n=0,0,len(nums)
        for i in nums:
            if i==0:
                zeroes+=1
            elif i==1:
                ones+=1
        for i in range(zeroes):
            nums[i]=0
        for i in range(zeroes,zeroes+ones):
            nums[i]=1
        for j in range(zeroes+ones,n):
            nums[j]=2