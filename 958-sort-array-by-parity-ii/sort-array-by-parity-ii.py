class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[x for x in nums if x%2==0]
        odd=[x for x in nums if x%2!=0]
        ans=[]
        ei,oi=0,0
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even[ei])
                ei+=1
            else:
                ans.append(odd[oi])
                oi+=1
        return ans
