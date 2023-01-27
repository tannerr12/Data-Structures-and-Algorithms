class Trie:
    
    def __init__(self, char):
        
        self.char = char
        self.adj = {}
        self.end = False
        

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """    
        words.sort()
        self.tri = Trie('')
        ans = set()
        
        for word in words:
            t = self.tri
            count = 0
            for char in word:
                
                if char in t.adj:
                    t = t.adj[char]

                else:
                    t.adj[char] = Trie(char)
                    t = t.adj[char]
                
            
           
            t.end = True
            
        """
        wset = set(words)  
        ans = set()
        """
        @cache
        def dfs(word,i,trie,count):
            
            if i >= len(word):
                return count

            res = 0
            if word[i] in trie.adj:
                trie = trie.adj[word[i]]
            #go down current Trie
        
                res = max(res,dfs(word, i+1, trie,count))
            
            #start new Trie
            if i < len(word) -1 and trie.end and word[i+1] in self.tri.adj:
                
                res = max(dfs(word, i+2, self.tri.adj[word[i+1]],count+1),res)
            
           # print(trie.char)
           # print(trie.end)
            return res
        
        """
        @cache
        def dfs(word,s,i):
            
            if i >= len(word):
                return s != word and s in wset

            res = False
           
            #not found
            res = res or dfs(word,s + word[i], i+1)
            
            if s in wset:
                #found
                res = res or dfs(word,word[i],i+1)
            
          
            return res
        
        
        for word in words:

            val = dfs(word,'', 0)
            
            if val:
                ans.add(word)
        
        
        return ans
            
        
            
                
            