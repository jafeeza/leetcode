class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)==0:
            return True
        intervals.sort()
        intial_s=intervals[0][0]
        intial_e=intervals[0][1]
        for i in intervals[1:]:
            s,e=i[0],i[1]
            if s>=intial_s and s>=intial_e and e>=intial_e:
                intial_s,intial_e=s,e
            else:
                return False
        return True