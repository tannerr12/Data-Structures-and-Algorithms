class trie:
    '''
    def __init__(self, char):
        
        self.char = char
        self.adj = {}
    '''
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ''' 
        mp = trie('')
        group = defaultdict(list)
        for word in dictionary:
            group[word[0]].append(word)
            mpp = mp
            for w in word:
                
                if w in mpp.adj:
                    mpp = mpp.adj[w]
                else:
                    mpp.adj[w] = trie(w)
                    mpp = mpp.adj[w]
        
        '''
        
        group = defaultdict(list)
        for word in dictionary:
            group[word[0]].append(word)
        pot = defaultdict(list)
        
        @cache
        def dfs(i,w,j):
            nonlocal pot
            if j >= len(w):
                pot[len(w)].append(w)
                return w
            if i >= len(s):
                return ''
            
            res = ''
            while i < len(s) and s[i] != w[j]:
                i+=1
            
            if i < len(s):
                res = max(res,dfs(i+1, w, j+1))
            
            return res 
        
        #print(group)
        
        res = ''
        seen = set()
        for i in range(len(s)):
            w = s[i]
            if w in seen:
                continue
            seen.add(w)
            for word in group[w[0]]:
                dfs(i + 1,word,1)
        
        res = '{'
       
        if pot:
            for val in pot[max(pot)]:
                res = min(res, val)
        
        return res if res != '{' else ''
                
            
        
        