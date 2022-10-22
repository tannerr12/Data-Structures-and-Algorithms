class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k == len(num):
            return '0'
        
        
        
        res = ''
        stack = []
        i = 0
        while i < len(num):
            

                
      
            while stack and k != 0 and num[i] < stack[-1]:
                    stack.pop()
                    k-=1
               
            
            
            stack.append(num[i])
                
          
            i+=1
        
        
        
        
        
        while stack and k != 0:
            stack.pop()
            k-=1
        j = 0
        
        while stack and j < len(stack) -1 and stack[j] == '0':
            j+=1
      

       
        return ''.join(stack[j:])