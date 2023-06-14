class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        debt = defaultdict(int)
        
        for x,y,z in transactions:
            debt[x] -= z
            debt[y] += z
        
        #print(debt)
        
        owes = defaultdict(int)
        has = defaultdict(int)
        
        for key,val in debt.items():
            if val < 0:
                owes[key] = abs(val)
            elif val > 0:
                has[key] = val
                
        ha = list(has.values())
        owe = list(owes.values())
        mask = 2 ** len(owe)
        mask -=1
        

        @cache
        def dfs(m,m2):
            
            if m == mask: 
                return 0
            res = float('inf')
            for i in range(len(ha)):
                if m2 & (1 << i) > 0:
                    continue
                for j in range(len(owe)):
                    if m & (1 << j) > 0:
                        continue
     
                    sub = min(ha[i], owe[j])
                    ha[i] -= sub
                    owe[j] -= sub
                    if owe[j] == 0 and ha[i]== 0:
                        res = min(res, dfs(m | (1 << j), m2 | (1 << i)) + 1)
                    elif ha[i] == 0:
                        res = min(res, dfs(m, m2 | (1 << i)) + 1)
                    elif owe[j] == 0:
                        res = min(res, dfs(m | (1 << j), m2) + 1)
                    else:
                        res = min(res, dfs(m,m2) + 1)
                    
                    ha[i] += sub
                    owe[j] += sub
                    
            return res
       
        ha.sort()
        owe.sort()
        #print(ha)
        #print(owe)
        
        
        return dfs(0,0)                           
            
            