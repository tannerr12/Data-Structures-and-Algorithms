class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        adj = defaultdict(set)

        for i in range(len(s1)):
            adj[s1[i]].add(s2[i])
            adj[s2[i]].add(s1[i])


    


        m = 'zz'
        seen = set()
        h = {}
        def dfs(i):
            nonlocal m
            if i in seen:
                return i

            
            m = min(m,i)
            seen.add(i)
            for x in adj[i]:

                dfs(x)

        
        res = ''
        for c in range(len(baseStr)):
            if c in h:
                res+= h[c]
                continue

            m = 'zz'
            dfs(baseStr[c])
            for val in seen:
                h[val] = m

            seen = set()    
            res += m
        

        return res


