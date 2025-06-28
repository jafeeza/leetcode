class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=defaultdict(int)
        for num in nums:
            h[num]+=1
        return max(h,key=h.get)
        