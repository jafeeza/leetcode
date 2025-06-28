class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=defaultdict(int)
        for num in nums:
            h[num]+=1
        for k,v in h.items():
            if v>len(nums)/2:
                return k
        return 0
        