class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        
        
        res = []
        val = 0
        for i in range(1, len(encoded) + 2):
            
            val ^= i
            
           
        
        
        #print(val)
        perm = [0] * (len(encoded) +1)
        
        perm[0] 
        p = val
        for i in range(1,len(encoded),2):
            p ^= encoded[i]
        
        perm[0] = p
        
        for i in range(1,len(encoded)+1):
            perm[i] = perm[i-1] ^ encoded[i-1]
        
        
        return perm