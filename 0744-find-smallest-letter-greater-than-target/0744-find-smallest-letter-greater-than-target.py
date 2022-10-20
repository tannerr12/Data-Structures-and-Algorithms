class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        
        
        
        
        l,r = 0, len(letters) -1
        
        res = float('inf')
        
        while l <= r:
            
            curr = (l+r) // 2
            
            
            char = letters[curr] 
            
            if ord(char) > ord(target):
                res = min(res, ord(char) - ord(target))
            
            
            if ord(char) > ord(target):
                r = curr -1
                
            else:
                l = curr +1
                
        
        
        if res != float('inf'):
            return chr(res + ord(target))
        
        else:
            return letters[0]