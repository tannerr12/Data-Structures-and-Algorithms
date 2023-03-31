class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        for i in range(len(queries)):
            
            queries[i].append(i)
            
            
        queries.sort()
        
        q1 = deque(nums)  
        q2 = deque()
        time = 0
        turn = 0
        
        res = [-1] * len(queries)
        for t,j,i in queries:
            
            while time < t:
                
                if not q1:
                    turn = 1
                elif not q2:
                    turn = 0
                    
                if turn == 0 and q1:
                    q2.append(q1.popleft())

                elif turn == 1 and q2:
                    q1.append(q2.popleft())

                time +=1
            
           
            if j < len(q1):
                ans = q1[j]
                res[i] = ans
                

        return res
                
        