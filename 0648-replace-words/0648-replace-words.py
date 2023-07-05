class Trie:
    
    def __init__(self,char):
        self.char = char
        self.adj = {}
        self.EOW = False
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        tri = Trie('')
        
        for word in dictionary:
            t = tri      
            for char in word:
                if char in t.adj:
                    t = t.adj[char]
                else:
                    t.adj[char] = Trie(char)
                    t = t.adj[char]
            
            t.EOW = True
        
        
        res = []
        words = sentence.split(' ')

        for word in words:
            t = tri        
            found = False
            for i in range(len(word)):
                if t.EOW == True:
                    res.append(word[:i])
                    found = True
                    break
                if word[i] in t.adj:
                    t = t.adj[word[i]]
                else:
                    break
            
            if not found:
                res.append(word)
        
        return ' '.join(res)
                
        
                