class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        res = 0
        memo = {}
        d = set()
        res = 0
        @cache
        def permu(s,z,y):
            nonlocal res
            if z >= len(realArr):
                return len(s)
            
            res = max(res,len(s))
            a= 0
            b = 0
            
            h = Counter(s)
            for j in range(z,len(realArr)):
                
                if j == y:
                    continue
                
                valid = True
                
                for y in realArr[j]:
                    
                    if y in h:
                        valid = False
                        break
                
                if valid:
                    
                    a = permu(s + realArr[j],j+1, j) 
                if realArr[j] not in d:
                    d.add(realArr[j])
                    b = permu(realArr[j], 0, j)
                
                
                    
            
            
            return max(a,b)
        
        
        realArr = []
        for i in range(len(arr)):
            temp =Counter(arr[i])
            if max(temp.values()) == 1:
                realArr.append(arr[i])
        
        
        
        if len(realArr) == 0:
            return 0
        val = permu(realArr[0], 0, 0)
        return res
        if val == 0:
            return len(max(realArr))
        else:
            val
                    
                
                
                
                
                
                
                
            
            
            
            