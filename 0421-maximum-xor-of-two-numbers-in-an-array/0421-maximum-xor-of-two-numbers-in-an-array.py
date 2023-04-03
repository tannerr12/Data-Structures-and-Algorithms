class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        binary search might work
        local =0 
        
        mx = 0
        h = {}
        
        prefix = []
        prefix.append(0)
        for i in range(len(nums)):
            prefix.append(prefix[-1] ^ nums[i])
            for j in range(i+1, len(nums)):
                h[(i,j)] = nums[i] ^ nums[j]
                
            
        
        print(h)
        print(prefix)
        
            #local = nums[i] ^ local
            
            
            #mx = max(mx,local)
            
        
        
        #return mx
        
        """
        #the answer has to be a number with the largest bit
        
        
        mask,output = 0,0
        
        for i in range(32,-1,-1):
            mask = mask | 1 << i
            #is that bit turned on
            found = set([n & mask for n in nums])
            #turn the bit on
            temp = output | 1 << i
                
            for f in found:
                if f ^temp in found:
                    output = temp
        
        return output