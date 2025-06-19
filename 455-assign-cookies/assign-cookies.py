class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c_c=0
        cI=0
        while cI<len(s) and c_c<len(g):
            if g[c_c]<=s[cI]:
                c_c+=1
            cI+=1
        return c_c  
