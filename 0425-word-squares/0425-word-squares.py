class Trie:
    
    def __init__(self,char):
        self.char = char
        self.adj = {}
        self.words = []
        
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        #ball
        #area
        #lead
        #lady
        
        tri = Trie('')
        
        for w in words:
            t = tri
            for char in w:
                if char in t.adj:
                    t = t.adj[char]
                    t.words.append(w)
                else:
                    t.adj[char] = Trie(char)
                    t = t.adj[char]
                    t.words.append(w)
        
        
        res = []
        
        q = deque()
        for w in words:
            q.append([w])
            
        while q:
            
            for _ in range(len(q)):
                ls = q.popleft()
                
                if len(ls) == len(ls[0]):
                    res.append(ls)
                    continue
                
               
                t = tri
                found = True
                for word in ls:
                    if word[len(ls)] in t.adj:
                        t = t.adj[word[len(ls)]]
                    else:
                        found = False
                        break

                if found:
                    for word in t.words:
                        l = ls.copy()
                        l.append(word)
                        q.append(l)
                
                
        return res
                
            
        
            
            