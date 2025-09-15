class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        res=len(l)
        for i in l:
            for j in i:
                if j in brokenLetters:
                    res-=1
                    break
        return res