class TwoSum:

    def __init__(self):
        self.arr=[]

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        n=len(self.arr)
        self.arr.sort()
        l,h=0,n-1
        while l<h:
            currs=self.arr[l]+self.arr[h]
            if currs<value:
                l+=1
            elif currs>value:
                h-=1
            else:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)