class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set()
        for val in deadends:
            dead.add(tuple(val))
        tar = tuple(target)
        q = deque()
        
        q.append(('0','0','0','0'))
        
        if q[0] in dead:
            return -1
        visited = set()
        level = 0
        while q:
            
            for i in range(len(q)):
                
                comb = q.popleft()
               
                if comb == tar:
                    return level
                
                for i in range(4):
                    
                    # check up and down
                    s = int(comb[i])
                    s = (s + 1) % 10
                    newTup = None
                    if i == 0:
                        newTup = (str(s),comb[1],comb[2],comb[3])
                    elif i == 1:
                        newTup = (comb[0],str(s),comb[2],comb[3])
                    elif i == 2:
                        newTup = (comb[0],comb[1],str(s),comb[3])
                    else:
                        newTup = (comb[0],comb[1],comb[2],str(s))
                    if newTup not in visited and newTup not in dead:
                        visited.add(newTup)
                        q.append(newTup)
                    
                    #check down
                    s = int(comb[i])
                    s = (s - 1) % 10
                    newTup = None
                    if i == 0:
                        newTup = (str(s),comb[1],comb[2],comb[3])
                    elif i == 1:
                        newTup = (comb[0],str(s),comb[2],comb[3])
                    elif i == 2:
                        newTup = (comb[0],comb[1],str(s),comb[3])
                    else:
                        newTup = (comb[0],comb[1],comb[2],str(s))
                    if newTup not in visited and newTup not in dead:
                        visited.add(newTup)
                        q.append(newTup)
                    
                
            level +=1
        
        return -1
                    
        