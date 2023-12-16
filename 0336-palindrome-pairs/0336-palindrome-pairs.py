class trie:
    
    def __init__(self, val):
        self.val = val
        self.adj = {}
        self.endWords = []
        self.endingWord = -1
    
        
        

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
     
        t = trie('')
        palis = []
        for i,word in enumerate(words):
            tri = t
            w = word[::-1]
            if word == w:
                palis.append(i)
            for j,char in enumerate(w):
                ispaliw = w[j:]
                ispali = ispaliw == ispaliw[::-1]

                if ispali:
                    tri.endWords.append(i)
                if char in tri.adj:
                    tri = tri.adj[char]
                
                else:
                    tri.adj[char] = trie(char)
                    tri = tri.adj[char]
                        
                      
            tri.endWords.append(i)
            tri.endingWord = i
        added = set()
        ans = []
        for i,w in enumerate(words):
            
            tri = t
            found = True
            for j,char in enumerate(w):
                
                if tri.endingWord != -1:
                    if w[j:] == w[j:][::-1] and (i,tri.endingWord) not in added:
                        added.add((i,tri.endingWord))
                        ans.append([i, tri.endingWord])
                if char in tri.adj:
                    tri = tri.adj[char]
                else:
                    found = False
                    break
            
            
            if found:
                if w == '':
                    for val in palis:
                        if i == val:
                            continue
                        if (i,val) not in added:
                            added.add((i,val))
                            ans.append([i,val])
                        if (val, i) not in added:
                            added.add((val,i))
                            ans.append([val,i])
                else:
                    for val in tri.endWords:
                        if val != i:
                            if (i, val) not in added:
                                ans.append([i,val])
                                added.add((i,val))

        
        return ans