class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        zero = 0
        one = 0
        
        for i in range(len(students)):
            if students[i] == 1:
                one+=1
            else:
                zero+=1
                
        
        for i in range(len(sandwiches)):
            
            if sandwiches[i] == 1 and one > 0:
                one -= 1
            elif sandwiches[i] == 0 and zero > 0:
                zero -= 1
            else:
                return len(sandwiches) - i
        
        return 0
        