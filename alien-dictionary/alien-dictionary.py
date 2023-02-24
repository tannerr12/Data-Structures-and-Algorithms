class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #1 create adjacent values by character each character will have a set saying it comes after
        #2 Loop through using dfs for each values after adj and if any value from before shows up before we reach the end we 
        #exit
        #3 as we go through the adjacencies lets append them to a result output
        
        #also do ranking for same word
        adj = defaultdict(set)
        indegree = defaultdict(int)
        for i,e in enumerate(words):
            
            for w in words[i]:
                if w not in indegree:
                    indegree[w] = 0
            for j in range(i + 1, len(words)):
                l= 0
                while l < len(words[i]) and l < len(words[j]):

                    if words[i][l] != words[j][l] and words[j][l] not in adj[words[i][l]]:
                        adj[words[i][l]].add(words[j][l])
                        indegree[words[j][l]] +=1
                        break
                    elif words[i][l] != words[j][l]:
                        break
                    l+=1
                
                if l == len(words[j]) and l < len(words[i]):
                    return ""
        
        #print(adj)
        #print(indegree)
        
        q = deque()
        
        for key,val in indegree.items():
            if val == 0:
                q.append(key)
                
        seen = set()
        res = []
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                res.append(node)
                seen.add(node)
                for val in adj[node]:
                    if val in seen:
                        continue
                    indegree[val] -=1
                    if indegree[val] == 0:
                        q.append(val)
        
      
        return ''.join(res) if sum(indegree.values()) == 0 else ""