class Solution:
    def generateSentences(self, sy: List[List[str]], text: str) -> List[str]:
        
        
        parent = {}
        rank = defaultdict(int)
        
        def find(x):
            
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            
            return parent[x]
        
        
        
        def union(x,y):
            
            p1,p2 = find(x),find(y)
            
            
            if p1 != p2:
                
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                
                elif rank[p2] > rank[p1]:
                    parent[p2] = p1
                    
                else:
                    rank[p1] += 1
                    parent[p2] = p1
                    
        
        
        for x,y in sy:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
                
            union(x,y)
        
        
        for x,y in sy:
            find(x)
            find(y)
        
        
        #print(parent)
        
        groups = defaultdict(list)
        
        for key,val in parent.items():
            groups[val].append(key)
        
        #print(groups)
        for key in groups:
            groups[key].sort()
            
        sentence = text.split(' ')
        
        #print(sentence)
        ans = []
        
        def dfs(i, cur):
            
            if i >= len(sentence):
                ans.append(cur)
                return
            
            before = cur
            if sentence[i] in parent:
                
                for val in groups[parent[sentence[i]]]:
                    if i < len(sentence) -1:
                        cur += val + ' '
                    else:
                        cur += val
                    
                    dfs(i+1, cur)
                    
                    cur = before
            else:
                if i < len(sentence) -1:
                    cur += sentence[i] + ' '
                else:
                    cur += sentence[i]
                    
                dfs(i+1, cur)
                
                #cur = before
                
        
        dfs(0,'')
        return ans
        