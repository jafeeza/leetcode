from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s=[]
        for n in nums:
            while s:
                g=gcd(s[-1],n)
                if g==1:
                    break
                n=(s.pop()*n)//g
            s.append(n)
        return s