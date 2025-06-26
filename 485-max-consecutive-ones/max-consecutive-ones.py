class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        clarge=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                c+=1
            else:
                if c>clarge:
                    clarge=c
                c=0
        if c>clarge:
            clarge=c
        return clarge
