class trie:
    
    def __init__(self, val):
        self.val = val
        self.adj = {}
        self.endWords = []
        self.endingWord = -1
    
        
        

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
     
        t = trie('')
     
        for i,word in enumerate(words):
            tri = t
            word = word[::-1]

            for j,char in enumerate(word):
       

                if word[j:] == word[j:][::-1]:
                    tri.endWords.append(i)
                if char in tri.adj:
                    tri = tri.adj[char]
                else:
                    tri.adj[char] = trie(char)
                    tri = tri.adj[char]
                        
                      
            tri.endingWord = i
  
        ans = []
        for i,w in enumerate(words):
            
            tri = t
            found = True
            for j,char in enumerate(w):
                
                if tri.endingWord != -1:
                    if w[j:] == w[j:][::-1]:
                        ans.append([i, tri.endingWord])
                        
                if char in tri.adj:
                    tri = tri.adj[char]
                else:
                    found = False
                    break
            
            
            if found:
                if tri.endingWord != -1 and tri.endingWord != i:
                    ans.append([i, tri.endingWord])
                
                for j in tri.endWords:
                    ans.append([i,j])
                

        
        return ans