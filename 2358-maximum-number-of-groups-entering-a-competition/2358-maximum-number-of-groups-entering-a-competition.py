class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        groups = []
        temp = []
        while grades:
            
            val = heappop(grades)
            temp.append(val)
            
            if len(groups) == 0 or len(groups[-1]) == len(temp) -1:
                groups.append(temp)
                temp = []
        
        #print(groups)
        
        #if temp and sum(temp) > sum(groups[-1]):
        #    groups.append(temp)
        return len(groups)
            
            