class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res=len(fruits)
        visit=[False for _ in range(len(baskets))]
        for i in range(len(fruits)):
            for j in range(0,len(baskets)):
                if fruits[i]<=baskets[j] and visit[j]==False:
                    visit[j]=True
                    res-=1
                    break
        return res
