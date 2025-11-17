class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count=k
        i=0
        while i<len(nums):
            if nums[i]==1:
                if count<k:
                    return False
                count=0
            else:
                count+=1
            i+=1
        return True

