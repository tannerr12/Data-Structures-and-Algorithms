class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        d = set()
        
        def permu(i):
           
            if i >= len(arr):
                return len(d)
            
            
            res = 0
            if checkArr(d, arr[i]):
                for char in arr[i]:
                    d.add(char)
                    
                res = permu(i+1)
            
                for char in arr[i]:
                    d.remove(char)
            
            res = max(res,permu(i+1))
               
            
            return res
        
        
        
        def checkArr(char,s):
                
            tempSet = set()
            for i in range(len(s)):

                if s[i] in tempSet or s[i] in char:
                    return False
                tempSet.add(s[i])


            return True
     
        
        
       
        return permu(0)
     
        
                    
                
                
                
                
                
                
                
            
            
            
            