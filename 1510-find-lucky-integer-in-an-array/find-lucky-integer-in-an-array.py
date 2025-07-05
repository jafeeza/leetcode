class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        s=set(arr)
        print(arr,s)
        c=0
        maxvalue=-1
        for i in s:
            for j in range(len(arr)):
                if i==arr[j]:
                    c+=1
            if i==c:
                maxvalue=max(maxvalue,i)
            c=0
        return maxvalue


