class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        nums.sort()
        minimum_integer=nums[0]
        print(nums[0])
        result=-1
        sum=0
        while minimum_integer>0 or sum>10:
            if minimum_integer==0:
                minimum_integer=sum
                sum=0
            sum+=minimum_integer%10
            minimum_integer//=10
        if sum%2==0:
            return 1
        else:
            return 0
