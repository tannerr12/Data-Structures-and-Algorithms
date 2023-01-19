class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        #create a not it stack 
        stack = deque()
        stackIt = deque()
        res = 0
        for i,p in enumerate(team):
            
            if p == 0:
                stack.append(i)
            
            else:
                stackIt.append(i)
                
            while stackIt and stack and stack[0] < stackIt[0] - dist and stack[0] < stackIt[0]:
                stack.popleft()
            while stackIt and stack and stack[0] > stackIt[-1] + dist:
                stackIt.popleft()
            
            if stack and stackIt:
                stack.popleft()
                stackIt.popleft()
                res +=1
            

            
            
        return res