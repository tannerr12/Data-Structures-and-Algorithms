class Trie:
    
    def __init__(self,c):
        
        self.char = c
        self.adj = {}
        self.end = False
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        h = Trie('')
        for i in range(len(words)):
            t = h
        
            for char in words[i]:
                if char not in t.adj:
                    t.adj[char] = Trie(char)
                    t = t.adj[char]
                else:
                    t = t.adj[char]
            
            t.end = True
        
        #print(h.adj)
        words.sort(key=lambda item: (-len(item), item))
        #print(words)
        
        
        def search(word):
            t = h
            for char in word:
                if char in t.adj:
                    t = t.adj[char]
                    if t.end == False:
                        return False
                else:
                    return False
            
            return True
                
            
        for word in words:
            
            if search(word):
                return word
        
        
        return ''
            
                
        
        