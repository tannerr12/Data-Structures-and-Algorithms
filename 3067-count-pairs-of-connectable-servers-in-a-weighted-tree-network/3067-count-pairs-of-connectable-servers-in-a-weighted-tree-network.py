class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for source,dest,weight in edges:
            adj[source].append([dest, weight])
            adj[dest].append([source, weight])
            
        
        def dfs(node, val, par, path):
            nonlocal ans
            
            if val == 0:
                ans += dct[0] - dct[(path, 0)]
            
            
            for child,w in adj[node]:
                if child == par:
                    continue
                if par == -1:
                    path += 1
                dfs(child, (val + w) % signalSpeed, node, path)
            
            if par != -1 and val == 0:
                dct[val] += 1
                dct[(path, val)] += 1
            
        dct = defaultdict(int)
        res = [0] * (len(edges) + 1)
        for i in range(len(edges) + 1):
            ans = 0
            
            dfs(i, 0, -1,0)
            
            res[i] = ans
            dct = defaultdict(int)
        
        return res
            
        
            
            
        