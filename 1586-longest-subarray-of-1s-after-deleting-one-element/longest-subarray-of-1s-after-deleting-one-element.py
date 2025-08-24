class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        maxlength=0
        count=0
        j=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                count+=1
            while(count>1):
                if nums[j]==0:
                    count-=1
                j+=1
            maxlength=max(maxlength,i-j)
        return maxlength

            