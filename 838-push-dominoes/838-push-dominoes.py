class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque()
        dominoes = list(dominoes)
        for i, dom in enumerate(dominoes):
            if dom != '.':
                q.append((i,dom))
            
            
        
        
        while q:

                ind,val = q.popleft()
                
                if ind > 0 and dominoes[ind -1] == '.' and val == 'L':
                    q.append((ind -1, 'L' ))
                    dominoes[ind -1] = 'L'
                elif val == 'R':
                    if ind + 1 < len(dominoes) and dominoes[ind +1] == '.':
                        if ind+ 2  < len(dominoes) and dominoes[ind + 2] == 'L':
                            q.popleft()
                        else:
                            q.append((ind +1, 'R'))
                            dominoes[ind +1] = 'R'

        
        return ''.join(dominoes)
                    
                

        
            