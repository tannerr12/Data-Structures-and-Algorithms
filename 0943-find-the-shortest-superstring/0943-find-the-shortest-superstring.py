class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
        overlap = defaultdict(lambda:defaultdict(int))
        #12 * 12 * 20 * 20
        for i in range(len(words)):
            
            for j in range(len(words)):
                if i == j:
                    continue
                
                score = 0
                for k in range(len(words[i])):
                    #print(words[i][len(words[i]) - k - 1:])
                    #print(words[j][:k+1])
                    if words[i][len(words[i]) - k - 1:] == words[j][:k+1]:
                        score = k+1
                        
                
                
                overlap[i][j] = score
        
        
        #print(overlap)
        mp = 2 ** len(words) -1
        ans = []
        st = ''
        
        @cache
        def dfs(i,bitmap):
            #nonlocal st
            if bitmap == 0:
                return 0
        
            res = float('-inf')
            for pos,sc in overlap[i].items():    
                if bitmap & (1 << pos) > 0:
                    res = max(res, dfs(pos,bitmap ^ (1 << pos)) + sc)
            
            return res
    
        res = float('-inf')
        start = -1
        for i in range(len(words)):
            score = dfs(i, mp ^ (1 << i))
            if score > res:
                res = score
                start = i
        
        
        final = []
        
        @cache
        def dfs2(i,bitmap,sc):
            nonlocal res,final
            if bitmap == 0:
                if sc == res:
                    final = ans.copy()
                
                return 0
            
            if len(final) > 0:
                return 0
                    
    
            for pos,sco in overlap[i].items():    
                if bitmap & (1 << pos) > 0:
                    ans.append(pos)
                    dfs2(pos,bitmap ^ (1 << pos),sc + sco) 
                    ans.pop()
                    
        
    
        ans.append(start)
        dfs2(start, mp ^ (1 << start), 0)
        #print(final)
        
        w = ''
        for i in range(len(final) -1):
            #print(words[final[i]][:-overlap[final[i]][final[i+1]]] )
            if overlap[final[i]][final[i+1]] > 0:
                w += words[final[i]][:-overlap[final[i]][final[i+1]]] 
            else:
                w += words[final[i]]
                
        w += words[final[-1]]
        return w
        
        
            
                