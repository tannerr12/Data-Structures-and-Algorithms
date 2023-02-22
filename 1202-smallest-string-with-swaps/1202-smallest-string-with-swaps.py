class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        parent = [i for i in range(len(s))]
        rank = [1] * len(s)
        
        
        def find(val):
            
            if val == parent[val]:
                return val
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x,y):
            
            v1,v2 = find(x),find(y)
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] +=1
                
        
        for x,y in pairs:
            union(x,y)
        for i in range(len(s)):
            find(i)
        
        ls = defaultdict(list)
        for i in range(len(s)):
            heappush(ls[parent[i]], s[i])
        
       # print(ls)
        res = []
        for i in range(len(s)):
            res.append(heappop(ls[parent[i]]))
        
       # print(res)
        
        #print(parent)
        return ''.join(res)