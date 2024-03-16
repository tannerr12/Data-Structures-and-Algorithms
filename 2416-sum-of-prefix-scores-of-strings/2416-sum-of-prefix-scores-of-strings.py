class trie:
    
    def __init__(self,val):
        self.val = val
        self.adj = {}
        self.count = 1
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        #wl = words.copy()
        
        #wl.sort(key=lambda x:(-len(x), x))

        #print(wl)
        
        t = trie('')
     
        for i in range(len(words)):
            tri = t
            for j in range(len(words[i])):
                char = words[i][j]
                if char in tri.adj:
                    tri = tri.adj[char]
                    tri.count += 1
                else:
                    tri.adj[char] = trie(char)
                    tri = tri.adj[char]
           
        
        ans = [0] * len(words)
        
        for i in range(len(words)):
            tri = t
            total = 0
            #search trie
            for char in words[i]:
                tri = tri.adj[char]
                total += tri.count
            
            ans[i] = total
        
        return ans
                
        