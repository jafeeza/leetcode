class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left,right=1,max(time)*totalTrips

        def E_time(given_time):
            actual_trips=0
            for i in time:
                actual_trips+=given_time//i
            return actual_trips>=totalTrips
        
        while left<right:
            mid=(left+right)//2
            if E_time(mid):
                right=mid
            else:
                left=mid+1
        return left