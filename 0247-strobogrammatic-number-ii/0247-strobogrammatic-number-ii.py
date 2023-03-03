class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        #go left to right on all numbers and add the same number to the front and back as we 
        res = []
        
    
        def dfs(num):
            
            if len(num) == n:
                if num[0] == '0' and len(num) > 1:
                    return
                res.append(num)
                return 
            
            
            for i in range(10):
                
                if n - len(num) == 1 and (i == 0 or i == 1 or i == 8):
                    dfs(num[:len(num)//2] + str(i) + num[len(num)//2:])
                
                if n - len(num) != 1:
                    if i == 6:
                        dfs(str(i) + num + '9')
                    elif i == 9:
                        dfs(str(i) + num + '6')
                    elif i == 1 or i == 8 or i == 0:
                        dfs(str(i) + num + str(i))
            
        
        dfs('')
        return res