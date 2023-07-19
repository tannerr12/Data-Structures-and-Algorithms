class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        
        
        #0,0,2
        #0D -> 0E -> 1O -> 0D -> 0E -> 1E -> 2O
        #we have repeated 0D and 0E
        
        MOD = 10 ** 9 + 7
        
        q = deque()
        q.append(0)
        
        counts = defaultdict(int)
        memo = {}
        level = 0
        while q:
            for i in range(len(q)):
                
                node = q.popleft()
                counts[node] +=1
                memo[(node,counts[node] % 2)] = level
                
                if len(counts) == len(nextVisit):
                    return level
                
                if counts[node] % 2:
                    if (nextVisit[node], (counts[nextVisit[node]] + 1) % 2) in memo:
                        level += level - memo[(nextVisit[node], (counts[nextVisit[node]] + 1) % 2)]
                        level %= MOD
                        q.append((node))
                    else:
                        q.append(nextVisit[node])
                
                else:
                    if (node + 1, (counts[node+1] + 1) % 2) in memo:
                        level += level - memo[(node + 1, (counts[node+1] + 1) % 2)]
                        level %= MOD
                        q.append(node)
                    else:
                        q.append((node+1) % len(nextVisit))
                
                
            level +=1
            level %= MOD
        
        
            