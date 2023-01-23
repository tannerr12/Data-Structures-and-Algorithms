class Solution:
    def confusingNumberII(self, n: int) -> int:
        #scan digits left -> right
        
        #current position in the string
        #was the last digit max of the number?

  
        def dfs(i,prevMax,s,v):
            
            if i >= len(str(s)):

                test = ''
                
                for j in range(len(v)-1,-1,-1):
                    if v[j] == '9':
                        test += '6'
                    elif v[j] == '6':
                        test += '9'
                    else:
                        test += v[j]
                
                if test != v:
                    return 1
                return 0
            
            highest = 9
            if prevMax:
                highest = int(s[i])
            
            res =0
            #9
            
            if highest >= 9:
                res += dfs(i+1,prevMax and int(s[i]) == 9,s,v + '9')
            if highest >= 6:
                res += dfs(i+1,prevMax and int(s[i]) == 6,s,v + '6')
            
            

                #8
            if highest >= 8:
                res += dfs(i+1,prevMax and int(s[i]) == 8,s,v + '8')
             

                #1
            if highest >= 1:
                res += dfs(i+1,prevMax and int(s[i]) == 1,s,v + '1')
                #0
            if highest >= 0 and i != 0:
                res += dfs(i+1,prevMax and int(s[i]) == 0,s,v + '0')

            
            return res
        
        
        
        res = dfs(0,True,str(n),'')
    
 
        s = '9'
        for i in range(len(str(n))-1):
         
            res += dfs(0,True,s * (i + 1),'')
          
        return res