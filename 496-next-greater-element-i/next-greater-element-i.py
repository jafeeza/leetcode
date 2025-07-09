class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        hashmap={}
        for num in nums2:
            while s and num>s[-1]:
                hashmap[s.pop()]=num
            s.append(num)
        return [hashmap.get(i,-1) for i in nums1]