class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi=[]
        sum_of=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                maxi.append(sum_of)
                sum_of=nums[i]
            else:
                sum_of+=nums[i]
        maxi.append(sum_of)
        return max(maxi)