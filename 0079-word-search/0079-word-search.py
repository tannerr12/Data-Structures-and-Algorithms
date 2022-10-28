class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        wordWidth = len(word) -1
        boardH = len(board) -1
        boardW = len(board[0]) -1
       
        if (boardH +1) * (boardW +1) < len(word):
            return False
        
        letterArr = [0] * 26
        for col in range(len(board)):
            
            for row in range(len(board[col])):
                char = board[col][row]
                if char.isupper():
                    letterArr[ord(char) - ord("A")] += 1
                else:
                    letterArr[ord(char) - ord("a")] += 1

                        
        for char in word:
                if char.isupper():
                    
                    if letterArr[ord(char) - ord("A")] ==  0: 
                        return False
                    else: letterArr[ord(char) - ord("A")] -= 1
                else:
                    if letterArr[ord(char) - ord("a")] == 0: 
                        return False
                    else: letterArr[ord(char) - ord("a")] -=1
                        
                        
        def backtrack(r,c,wi,visited):
            
            if r > len(board) -1 or r < 0 or c > len(board[0]) -1 or c < 0 or board[r][c] != word[wi] or visited[str(r) + "," + str(c)] or wi > wordWidth:
                return False
            
            if board[r][c] == word[len(word) -1] and wi == len(word) -1:
                return True
            visited[str(r) + "," + str(c)] = True
            res = (backtrack(r+1,c,wi+1,visited) or
            backtrack(r-1,c,wi+1,visited) or 
            backtrack(r,c+1,wi+1,visited) or 
            backtrack(r,c-1,wi+1,visited))
            visited[str(r) + "," + str(c)] = False
            
            return res
            
        
        for r in range(len(board)):
            
            for c in range(len(board[0])):
                
                if board[r][c] == word[0]:
                    if backtrack(r,c,0,collections.defaultdict(bool)):
                        return True
        
        
        return False
                                   
        