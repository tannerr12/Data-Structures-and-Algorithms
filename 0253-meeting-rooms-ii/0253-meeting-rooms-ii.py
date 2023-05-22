class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        l,r = 0,0
        res = 0
        count= 0
        
        
        while l < len(start) and r < len(end):
            if start[l] < end[r]:
                count +=1
                l+=1
            else:
                count-=1
                r+=1
            res = max(res,count)
        return res
