class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        rank = [0] * len(source)
        parent = [i for i in range(len(source))]
        
        
        def find(x):
            
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x,y):
            
            parx,pary = find(x),find(y)
            
            if parx != pary:
                
                if rank[parx] > rank[pary]:
                    parent[pary] = parx
                elif rank[pary] > rank[parx]:
                    parent[parx] = pary
                else:
                    if parx < pary:
                        parent[pary] = parx
                        rank[parx] += 1
                    else:
                        parent[parx] = pary
                        rank[pary] += 1
            
        def isConnected(x,y):
            return find(x) == find(y)
        
        
        for x,y in allowedSwaps:
            union(x,y)
        
        for i in range(len(parent)):
            find(i)
        
        mp = defaultdict(lambda:defaultdict(int))
        for i in range(len(source)):
            mp[parent[i]][source[i]] += 1
         
        #print(mp)
        #print(parent)

        res = 0
        for i in range(len(source)):
            if target[i] in mp[parent[i]] and mp[parent[i]][target[i]] > 0:
                mp[parent[i]][target[i]] -= 1
                res += 1
        
        return len(source) - res