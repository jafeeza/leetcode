class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res=0
        n=len(happiness)
        for i in range(0,k):
            if happiness[i]-i<=0:
                break
            res+=happiness[i]-i
        return res