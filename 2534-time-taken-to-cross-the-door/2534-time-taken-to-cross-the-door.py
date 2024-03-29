class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter = deque()
        exit = deque()
        
        time = arrival[0]
        prevt, prevType = -2,-2
        i = 0
        res = [0] * len(arrival)
        while i < len(arrival) or enter or exit:
            useType = False
            if prevt == time-1:
                useType = True
            
            prevt = time
            while i < len(arrival) and arrival[i] == time:
                if state[i] == 1:
                    exit.append((arrival[i],i))
                else:
                    enter.append((arrival[i],i))
                
                i +=1
            
            
            if useType:
                if prevType == 1 and exit:
                        val,j = exit.popleft()
                        res[j] = time
                        prevType = 1
                elif prevType == 0 and enter:
                        val,j = enter.popleft()
                        res[j] = time
                        prevType = 0
                elif exit:
                        val,j = exit.popleft()
                        res[j] = time
                        prevType = 1
                elif enter:
                        val,j = enter.popleft()
                        res[j] = time
                        prevType = 0
            else:
                if exit:
                        val,j = exit.popleft()
                        res[j] = time
                        prevType = 1
                elif enter:
                        val,j = enter.popleft()
                        res[j] = time
                        prevType = 0
                
            if i < len(arrival) and not exit and not enter:
                time = arrival[i]
            else:
                time +=1
        
        return res
                
                    
            
            
            
            
            
            
            
            
        
        