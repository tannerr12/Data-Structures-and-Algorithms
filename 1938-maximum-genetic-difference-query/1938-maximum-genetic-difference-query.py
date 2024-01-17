class trie:
    
    def __init__(self,val):
        
        self.adj = {}
        self.val = val
        
        
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        p = -1
        mx = 0
        for i in range(len(queries)):
            mp[queries[i][0]].append([queries[i][1], i])
            mx = max(mx, queries[i][1])
        self.adjs = defaultdict(list)
        for i in range(len(parents)):
            
            if parents[i] == -1:
                p = i
            else:
                self.adjs[parents[i]].append(i)
        #queries.sort()
        #self.t = trie()
        
        size = 19
        
        '''
        for i in range(len(parent)):
            tri = self.t
            for j in range(size + 1):
                if i & (1 << j) > 0:
                    if 1 in tri.adj:
                        tri = tri.adj[1]
                    else:
                        tri.adj[1] = trie(1)
                        tri = tri.adj[1]
                else:
                    if 0 in tri.adj:
                        tri = tri.adj[0]
                    else:
                        tri.adj[0] = trie(0)
                        tri = tri.adj[0]
            
            
        '''
    
        def dfs(node, tri):
            nonlocal size,ans
            if node is None:
                return None
            changes = []  # List to keep track of changes made to the trie
            tr = tri
            for j in range(size,-1,-1):
                if node & (1 << j) > 0:
                    if 1 in tri.adj:
                        tri = tri.adj[1]
                    else:
                        changes.append((tri, 1))
                        tri.adj[1] = trie(1)
                        tri = tri.adj[1]
                else:
                    if 0 in tri.adj:
                        tri = tri.adj[0]
                    else:
                        changes.append((tri, 0))
                        tri.adj[0] = trie(0)
                        tri = tri.adj[0]
            

                    
            for n in self.adjs[node]:
                dfs(n, tr)
            
            for val,idx in mp[node]:
                t = tr
                #print(t.adj)
                for j in range(size,-1,-1):
                    if val & (1 << j) > 0 and 0 in t.adj:
                        t = t.adj[0]
                    elif val & (1 << j) == 0 and 1 in t.adj:
                        t = t.adj[1]
                        val |= (1 << j)
                    else:
                        if val & (1 << j) > 0 and 1 in t.adj:
                            val ^= (1 << j)
                            t = t.adj[1]
                        elif 0 in t.adj:
                            t = t.adj[0]
                
                ans[idx] = val
            # Revert the trie to its previous state
            for tri_node, bit in reversed(changes):
                del tri_node.adj[bit]
            
                    
            
            
            
                
        ans = [0] * len(queries)
        dfs(p, trie(0))
        
        
        '''
        print(queries)
        for i in range(len(queries)):
            
            node,val,j = queries[i]
            mx = 0
            while node != -1:
                mx = max(mx, val ^ node)
                node = parents[node]
            
            ans[j] = mx
        
        '''
        return ans