class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ind=[]
        for i in range(0,len(nums)):
            if nums[i]==key:
                ind.append(i)
        res=[]
        for i in range(0,len(nums)):
            for j in range(0,len(ind)):
                if abs(i-ind[j])<=k:
                    res.append(i)
                    break
        return res