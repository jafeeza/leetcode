class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        pref=0
        for num in nums:
            pref=((pref<<1)+num)%5
            ans.append(pref==0)
        return ans
