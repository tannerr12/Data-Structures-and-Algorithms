class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        
        
        
        n,m = len(board), len(board[0])
        nn,mm = len(pattern), len(pattern[0])
        
        
        def scan(i,j):
            letters = defaultdict(int)
            lettersused = set()
            for k in range(i, i+nn):
                for l in range(j, j + mm):
                    c = pattern[k - i][l - j]
                    if c == str(board[k][l]):
                        continue
                    elif ord(c) >= ord('a'):
                        if (board[k][l] not in letters and c not in lettersused) or letters[board[k][l]] == c:
                            letters[board[k][l]] = c
                            lettersused.add(c)
                            continue
                        else:
                            return False
                    else:
                        return False
            
            return True
            
            
        for i in range(n - nn + 1):
            for j in range(m - mm + 1):
                
                if scan(i,j):
                    return [i,j]
                
            
            
        
        return [-1,-1]
        
        
        
                