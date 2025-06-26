class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[0]*n
        pi,ni=0,1
        for i in range(n):
            if nums[i]>0:
                r[pi]=nums[i]
                pi+=2
            else:
                r[ni]=nums[i]
                ni+=2
        return r

                    
