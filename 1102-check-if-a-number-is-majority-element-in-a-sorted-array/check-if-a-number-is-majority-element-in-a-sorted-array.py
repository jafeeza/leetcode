class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        return d.get(target,0)>len(nums)//2