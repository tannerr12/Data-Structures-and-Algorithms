class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        graph = defaultdict(list)
        if n == 1:
            return ''.join(map(str, range(k)))
        
        graph = defaultdict(list)
		# Use product to create the possible passwords
        for comb in product(range(k), repeat=n):
			# Each node has n-1 digits
			# Eg. if comb was 01001 (where n=4 and k=2)
			# We would add an edge from node 0100 to node 1001
            graph[tuple(comb[:-1])].append(tuple(comb[1:]))
        print(graph)
        ans = []
        def dfs(node):
            
            while graph[node]:
                dfs(graph[node].pop())
            
            ans.append(node[0])
            
        
        dfs(tuple([0]*(n-1)))
        
        ans.reverse()
        #ans += [0] * (n-2)
        ans = [str(val) for val in ans]
        return ''.join(ans) + ('0' * (n-2))
        
        