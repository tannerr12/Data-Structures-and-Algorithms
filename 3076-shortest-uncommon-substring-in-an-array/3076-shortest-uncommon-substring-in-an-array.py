class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans = [""] * len(arr)
        adj = defaultdict(set)
        counter = defaultdict(int)
        #bigset = set()
        for i in range(len(arr)):
            for size in range(1, len(arr[i])+1):
                for j in range(size, len(arr[i])+1):
                    word = arr[i][j-size:j]
                    if word not in adj[i]:
                        adj[i].add(word)
                        #bigset.add(word)
                        counter[word] += 1
        
        i = 0
        for key,val in adj.items():
            
            for word in sorted(val, key = lambda x: (len(x),x)):
                
                if counter[word] == 1:
                    ans[i] = word
                    break
            
            i += 1
        
        return ans
        
        
