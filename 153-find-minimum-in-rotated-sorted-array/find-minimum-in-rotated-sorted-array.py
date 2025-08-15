class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1           #[4,5,6,7,0,1,2]
        while l<r:
            m=(l+r)//2            #m=3,midd=[7]   [0,1,2]. m=3
            if nums[m]<nums[r]:  
                r=m                 #l=4,r=3
            else:                   #l=4,r=6
                l=m+1
        return nums[l]