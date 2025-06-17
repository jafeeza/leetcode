class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
            n=n*10+i
        n=n+1
        d=[]
        while n>0:
            d.append(n%10)
            n//=10
        d.reverse()
        return d