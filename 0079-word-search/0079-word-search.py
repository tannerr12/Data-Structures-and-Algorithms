class Trie:
    
    def __init__(self,c):
        
        self.char = c
        self.adj = {}
        self.end = False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        count = Counter(word)
        for r in range(len(board)):
            for c in range(len(board[0])): 
                if board[r][c] in count:
                    count[board[r][c]] -=1
                    
        if max(count.values()) > 0:
            return False
                
        h = Trie('')
        t = h
        for w in word:
            t.adj[w] = Trie(w)
            t = t.adj[w]
        
        
        t.end = True
        seen = set()
        def dfs(r,c,trie):
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in seen:
                return False

            if board[r][c] in trie.adj:
                trie = trie.adj[board[r][c]]
                if trie.end == True:
                    return True
            else:
                return False
            
            seen.add((r,c))            
            #4 direcitions

            res = dfs(r+1,c,trie) or dfs(r-1,c,trie) or dfs(r,c+1,trie) or dfs(r,c-1,trie)
            
            seen.remove((r,c))
            
            return res
            
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                
                if board[r][c] == word[0]:
                    
                    if dfs(r,c,h):
                        return True
                    
        
        
        return False
            
            
            
    
        
        
        