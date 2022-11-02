class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        adj = collections.defaultdict(set)
        
        
        bank.append(start)
       # bank.sort()
        h = {}
        
     #   for i in range(len(bank)):
            
     #       h[bank[i]] = Counter(bank[i])
        
        
     #   print(h)
        for i in range(len(bank)):
            
            for j in range(len(bank)):
                
                if i == j or bank[j] == start:
                    continue
                
                
                diffCount = 0
                
                for x in range(len(bank[i])):
                    
                    if bank[i][x] != bank[j][x]:
                        diffCount+=1
                
                
                if diffCount == 1:
                    adj[bank[i]].add(bank[j])
        
        
       # print(adj)
        
        seen = set()
        c = float('inf')
        def dfs(i,count):
            nonlocal c
            
            if i in seen:
                return 
            
            if i == end:
                c= min(c,count)
                return 
            seen.add(i)
            

            for x in adj[i]:
                
                dfs(x, count+1)
                
            
            
            seen.remove(i)
        
        
        for x in adj[start]:
            dfs(x,1)
        
        return c if c != float('inf') else -1
            
            
        
        
        
        
        