class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        arr = []
        num = 0
        c = 0
        for i in range(len(expression)):
            
            if expression[i] == '-' or expression[i] == '*' or expression[i] == '+':
                
                arr.append(num)
                num = 0
                arr.append(expression[i])
  
            else:
                num = num * 10 + int(expression[i])
        
        else:
            arr.append(num)
        
       
        
        def backtrack(left,right):
            
            if left == right:
                return [arr[left]]
            ans = []
            for i in range(left+1,right,2):
                r = backtrack(i+1,right)
                l = backtrack(left, i-1)
            
                if arr[i] == "*":
                    for k in l:
                        for j in r:
                            ans.append(k * j)
                               
                if arr[i] == '-':
                    for k in l:
                        for j in r:
                            ans.append(k - j)
                if arr[i] == "+":
                    for k in l:
                        for j in r:
                            ans.append(k + j)
            
            return ans
            
        return backtrack(0,len(arr)-1)
        
            
            
            
            
            