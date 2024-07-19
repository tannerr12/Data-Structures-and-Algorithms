class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        
        
        acount = defaultdict(int)
        bcount = defaultdict(int)
        ccount = defaultdict(int)
        
        def gather(num):
            bits = 0
            while num:
                
                num = num & (num-1)
                bits += 1
            
            return bits
        
        for val in a:
            
            if gather(val) % 2 == 0:
                acount[0] += 1
            else:
                acount[1] += 1
        
        for val in b:
            
            if gather(val) % 2 == 0:
                bcount[0] += 1
            else:
                bcount[1] += 1
        
        for val in c:
            
            if gather(val) % 2 == 0:
                ccount[0] += 1
            else:
                ccount[1] += 1
                
            
        res = 0
        for i in range(2):
            
            for j in range(2):
                
                for k in range(2):
                    if i + j + k == 0 or i + j + k == 2:
                        res += acount[i] * bcount[j] * ccount[k]
        
        return res
                        
                    
                    
            
        
        
            