class Trie:
    
    def __init__(self,val):
        self.char = val
        self.adj = {}


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        #only words of the same length matter
        #we want to try for large abreviations first such as first letter + 4 
        #maybe we can find letter positions that dont match since if any letter does not match our answer is always 2 or 3
        
        
        self.t = Trie('')
        
    
        def dfs(i,word,tri,last):
            if i >= len(word):
                return
            
            
            for j in range(2, len(word)-i+1):
                if last:
                    break
                ttri = tri
                if j in tri.adj:
                    ttri = tri.adj[j]
                else:
                    ttri.adj[j] = Trie(j)
                    ttri = tri.adj[j]
                
                dfs(i + j,word, ttri,True)
            
            if word[i] in tri.adj:
                tri = tri.adj[word[i]]
            else:
                tri.adj[word[i]] = Trie(word[i])
                tri =tri.adj[word[i]]
                
            dfs(i+1,word,tri,False)

        for word in dictionary:
            if len(word) == len(target):
                dfs(0,word,self.t,False)

        #print(self.t.adj)
        ans = []
        arr = []
        def dfs2(i,word,tri,last,new):
            nonlocal ans
            if new:
                if len(ans) == 0 or len(ans) > len(arr) + (len(target) - i > 0):
                    ans = arr.copy()
                    if len(target) - i > 0:
                        ans.append(str(len(target) - i)) 
                return
            elif i >= len(target):
                return

            
            for j in range(2, len(word)-i+1):
                if last:
                    break
                ttri = tri
                nnew = False
                if j in tri.adj:
                    ttri = tri.adj[j]
                else:
                    ttri.adj[j] = Trie(j)
                    ttri = tri.adj[j]
                    nnew = True
                arr.append(str(j))
                dfs2(i + j,word, ttri,True,nnew or new)
                arr.pop()
                
                
            nnew = False
            if word[i] in tri.adj:
                tri = tri.adj[word[i]]
            else:
                tri.adj[word[i]] = Trie(word[i])
                tri =tri.adj[word[i]]
                nnew = True
                
            arr.append(word[i])
            dfs2(i+1,word,tri,False,new or nnew)
            arr.pop()
        
        #print(self.t.adj[3].char)
        #print(self.t.adj[3].adj['u'].char)
        #print(self.t.adj[3].adj['u'].adj[3].char)
        dfs2(0,target, self.t,False,False)
        #print(ans)
        


        return ''.join(ans)