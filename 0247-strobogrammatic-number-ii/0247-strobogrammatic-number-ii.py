class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        #go left to right on all numbers and add the same number to the front and back for 1 8 or 0 as they rotate the same for 6 and 9 assign them opposite and for middle we can only use 0,1,8
        #if the start number is a 0 and its not length 1 skip it
        res = []
        
        ls = ['0','1','6','8','9']
        def dfs(num):
            
            if len(num) == n:
  
                res.append(num)
                return 
            
            
            for i in ls:
                
                if n - len(num) == 1 and (i == '0' or i == '1' or i == '8'):
                    dfs(num[:len(num)//2] + i + num[len(num)//2:])
                
                if n - len(num) != 1:
                    if i == '6':
                        dfs(i + num + '9')
                    elif i == '9':
                        dfs(i + num + '6')
                    elif i == '1' or i == '8' or (i == '0' and n - len(num) != 2 and n - len(num) != 3):
                        dfs(i + num + i)
            
        
        dfs('')
        return res