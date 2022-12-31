class Trie:
    
    def __init__(self, char):
        
        self.char = char
        self.adj = {}
        self.end = False
        

class MagicDictionary:

    def __init__(self):
        self.t = Trie('')
    def buildDict(self, dictionary: List[str]) -> None:
        temp = self.t
        for word in dictionary:
                        
            for char in word:
                if char in temp.adj:
                    temp = temp.adj[char]
                else:
                    temp.adj[char] = Trie(char)
                    temp = temp.adj[char]
            
            temp.end = True
            temp = self.t
        
        

    def dfs(self, i,skipped,word,t):
        if i >= len(word):
            return t.end and skipped
        
        res = False
        #choose original
        if word[i] in t.adj:
            temp= t
            t = t.adj[word[i]]
            res = res or self.dfs(i+1,skipped, word, t)
            t = temp
        #skip character
        if not skipped:
            for w in t.adj:
                if w == word[i]:
                    continue
                temp = t
                t = t.adj[w]
                res = res or self.dfs(i+1,True,word,t)
                t = temp
        
        
        return res
    def search(self, searchWord: str) -> bool:
        
        return self.dfs(0,False,searchWord, self.t)
            
            
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)