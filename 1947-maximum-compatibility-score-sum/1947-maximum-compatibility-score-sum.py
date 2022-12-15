class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        
        
        @cache
        def backtrack(i,bitmap):
            
            if i >= len(students):
                return 0
            
            res = 0
            for j in range(len(mentors)):
                
                if bitmap & (1 << j) == 0:
                    score = 0
                    for x,y in zip(students[i], mentors[j]):
                        if x == y:
                            score +=1
                    
                    res = max(res,backtrack(i+1, bitmap | (1 << j)) + score)
                
                
            
            
            return res
        
        return backtrack(0,0)

