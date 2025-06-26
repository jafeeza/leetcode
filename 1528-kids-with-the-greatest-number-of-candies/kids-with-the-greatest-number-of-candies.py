class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can=max(candies)
        n=len(candies)
        res=[False]*n
        for i in range(0,len(candies)):
            if candies[i]+extraCandies>=max_can:
                res[i]=True
        return res