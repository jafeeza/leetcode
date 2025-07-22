class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return sum(nums)
        elements=set()
        left=0
        curr_sum=0
        max_sum=0
        for right in range(len(nums)):
            while nums[right] in elements:
                curr_sum-=nums[left]
                elements.remove(nums[left])
                left+=1
            curr_sum+=nums[right]
            elements.add(nums[right])
            max_sum=max(max_sum,curr_sum)

        return max_sum
