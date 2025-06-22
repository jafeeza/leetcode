class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        r=[]
        for i in range(1,n+1):
            if n%i==0:
                r.append(i)
        if k<=len(r):
            return r[k-1]
        else:
            return -1