class trie:
    
    def __init__(self, char):
        
        self.adj = {}
        self.char = char
        self.eow = False
        self.count = 1

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        mp = defaultdict(lambda:trie(''))
        
        for w in words:
            tri = mp[str(len(w)) + w[-1]]
            for c in w:
                
                if c in tri.adj:
                    tri = tri.adj[c]
                    tri.count += 1
                    
                else:
                    tri.adj[c] = trie(c)
                    tri = tri.adj[c]
            
            tri.eow = True
        
        
        
        ans = []
        
        for i in range(len(words)):
            tri = mp[str(len(words[i])) + words[i][-1]]
            word = words[i]
            #print(tri.adj)
            #search the word
            for j in range(len(words[i]) -1):
                
                c = words[i][j]
                tri = tri.adj[c]
                
                if tri.count == 1:
                    num = len(words[i]) - j - 2
                    if num > 1:
                        word = words[i][:j+1] + str(num) + words[i][-1]
                    break
            
            ans.append(word)
        
        
        return ans
            
                