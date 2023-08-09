class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        groups,val = 0,0
        for i in range(1, 100000):
            if val + i <= len(grades):
                val += i
                groups += 1
            else:
                break
        
        return groups
            
            