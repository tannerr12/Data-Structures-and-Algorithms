class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        
        one = 0
        
        for val in data:
            
            if val == 1:
                one+=1
        
        
        l = 0
        cur = 0
        res = float('inf')
        for i in range(len(data)):
            
            cur += data[i]
            
            while i - l + 1 > one:
                
                cur -= data[l]
                l+=1
            
            
            if i -l +1 == one:
                res = min(res,one - cur)
        
        
        return res
            