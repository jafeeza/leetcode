class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarr=0
        ans=0
        for num in nums:
            if num==0:
                subarr+=1
            else:
                subarr=0
            ans+=subarr
        return ans