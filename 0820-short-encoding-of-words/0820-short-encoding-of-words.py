class trie:
    
    def __init__(self, val):
        self.val = val
        self.adj = {}
        self.eow = False
        self.size = 0
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        #words.sort(revierse=True)
        t = trie('')
        for word in words:
            tri = t
            word = word[::-1]
            for char in word:
                
                if char in tri.adj:
                    tri = tri.adj[char]
                else:
                    tri.adj[char] = trie(char)
                    tri = tri.adj[char]
            
            tri.eow = True
            tri.size = len(word)
        
        
        def dfs(tri):
            if len(tri.adj) == 0:
                return tri.size + 1
            res = 0
            for char in tri.adj:
                res += dfs(tri.adj[char])
            
            return res
        
        
        tri = t
        #print(t.adj)
        return dfs(tri)