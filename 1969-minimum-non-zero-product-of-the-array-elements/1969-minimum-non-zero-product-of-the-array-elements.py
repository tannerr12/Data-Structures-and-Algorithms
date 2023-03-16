class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        if p == 1:
            return 1
        
        MOD = 10 ** 9 + 7
        #since they are all complements of eachother we can guarantee half of them are shifted to 1 and the other half are shifted to mx -1
        #15
        mx = (2 ** p) -1
        
        # since mx is the compliment of 0 we have to skip those 2 otherwise our product would be 0. mx -1 is the next best bet
        #14
        high = mx -1
        
        # 7
        size = high // 2
        
        #14 * 7
        total = pow(high, size, MOD)
        
        #(14 ** 7) * 15
        total = (total * mx) % MOD
        
        return total
        