class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        max_freq=0
        for f in freq.values():
            max_freq=max(max_freq,f)
        count=0
        for fr in freq.values():
            if fr==max_freq:
                count+=1
        return count*max_freq