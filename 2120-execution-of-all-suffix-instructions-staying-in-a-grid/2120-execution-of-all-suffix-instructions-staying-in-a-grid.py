class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        def oob(i,j):
            if i < 0 or j < 0 or i >= n or j >= n:
                return True
            return False
        
        mp = {'R': [0,1], 'L': [0,-1], 'U': [-1,0], 'D': [1,0]}
        def solve(i):
            
            r,c = startPos[0],startPos[1]
            res = 0
            for j in range(i,len(s)):
                
                if not oob(r + mp[s[j]][0], c + mp[s[j]][1]):
                    r += mp[s[j]][0]
                    c += mp[s[j]][1]
                    res +=1
                else:
                    break
                    
            return res
        
        ans = []
        
        for i in range(len(s)):    
            ans.append(solve(i))
        
        
        return ans