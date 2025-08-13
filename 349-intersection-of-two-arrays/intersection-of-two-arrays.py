class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n=len(nums1)
        m=len(nums2)
        p1=0
        p2=0
        s=set()
        while p1<n and p2<m:
            if nums1[p1]==nums2[p2]:
                s.add(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
        l=[]
        for i in s:
            l.append(i)
        return l