class Trie:
    
    def __init__(self, char):
        self.char = char
        self.adj = {}
        self.words = {}
        

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.curWord = ''
        self.t = Trie('')
        self.tempt = self.t
        for s,t in zip(sentences, times):
            self.addWord(s,t)
        self.wordsSeen = set(sentences)
        #print(self.t.adj['i'].words)
        
    def input(self, c: str) -> List[str]:
        if c in self.tempt.adj:
            self.tempt = self.tempt.adj[c]
            self.curWord += c
            
            wrdls = sorted(self.tempt.words.items(), key= lambda x: (-x[1],x[0]))
            #print(wrdls)
            res = []
            for i in range(min(3,len(wrdls))):
                res.append(wrdls[i][0])
            
            return res
            
        elif c == '#':
            if self.curWord in self.wordsSeen:
                self.incrementWord(self.curWord)
                
            else: 
                self.addWord(self.curWord,1)
                self.wordsSeen.add(self.curWord)
            self.curWord = ''
            self.tempt = self.t
            return []
        else:
            self.curWord += c
            self.tempt = Trie('')
            return []
        
    
    def addWord(self,word,times):
        trie = self.t
        for char in word:
            
            if char in trie.adj:
                trie = trie.adj[char]
            else:
                trie.adj[char] = Trie(char)
                trie = trie.adj[char]
            
            trie.words[word] = times
        
    def incrementWord(self,word):
        trie = self.t
        for char in word:
            
            if char in trie.adj:
                trie = trie.adj[char]
            else:
                trie.adj[char] = Trie(char)
                trie = trie.adj[char]
            
            trie.words[word] += 1
            
        
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)