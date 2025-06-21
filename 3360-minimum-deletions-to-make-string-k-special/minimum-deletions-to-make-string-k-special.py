class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt=defaultdict(int)
        for c in word:
            cnt[c]+=1
        res=len(word)
        for a in cnt.values():
            d=0
            for b in cnt.values():
                if a>b:
                    d+=b
                elif b>a+k:
                    d+=b-(a+k)
            res=min(res,d)
        return res