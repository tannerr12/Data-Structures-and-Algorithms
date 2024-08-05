class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(lambda:defaultdict(int))
        
        for i in range(len(original)):
            
            org = original[i]
            ch = changed[i]
            if org in adj and ch in adj[org]:
                adj[org][ch] = min(adj[org][ch], cost[i])
            else:
                adj[org][ch] = cost[i]
            
        
        
        cache = defaultdict(int)

        def find(x):
            
            seen = set()
            q = []
            q.append((0,x))
            
            while q:
                
                c, cur = heappop(q)
                
                if cur in seen:
                    continue
                    
                seen.add(cur)
                cache[(x,cur)] = c
                
                
                for val in adj[cur]:
      
                    heappush(q, (c + adj[cur][val], val))
            
            
            
        
        for i in range(26):    
            ch1 = chr(i + ord('a'))
            find(ch1)
                
        
        res = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            c = cache[(source[i], target[i])]
            if c == 0:
                return -1
            
            res += c
        
        #print(cache)
        return res
            
                
                