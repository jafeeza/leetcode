class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        ar=0
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            ar=max(ar,h*w)
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return ar