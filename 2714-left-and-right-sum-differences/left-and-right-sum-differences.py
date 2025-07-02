class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        rightSum,leftSum=[0]*n,[0]*n
        sum1,sum2=0,0
        i,j=0,n-1
        while i<len(nums) and j>=0:
            leftSum[i]=sum1
            sum1+=nums[i]
            rightSum[j]=sum2
            sum2+=nums[j]
            i+=1
            j-=1
        absolute_differences = [abs(x - y) for x, y in zip(leftSum, rightSum)]
        return absolute_differences

        