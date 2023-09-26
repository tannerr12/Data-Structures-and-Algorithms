class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10 ** 9 + 7
        
        has0 = 0
        ends0 = 0
        ends1 = 0
        
        for i in range(len(binary)):
            
            if binary[i] == '0':
                ends0 = (ends0 + ends1) % MOD
                has0 = True
            else:
                ends1 = (ends0 + ends1 + 1) % MOD  
                
        
        return (ends0 + ends1 + has0) % MOD
        #11011
        #1 - > 1
        #