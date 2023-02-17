class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        adj = defaultdict(int)
        
        for x,y in pairs:
            adj[x] = y
            adj[y] = x
            
        
        checked = defaultdict(set)
        res = 0
        paired = set()
        for i in range(n):
            j = 0
            while preferences[i][j] != adj[i]:
                neigh = preferences[i][j]
                if i in checked[neigh]:
                    paired.add(i)
                    paired.add(neigh)
                checked[i].add(neigh)
                j+=1
            #scan over both preferences
        
        
        
        #print(checked)
        return len(paired)
        
            
        
        #2,3
        #2,1
        #