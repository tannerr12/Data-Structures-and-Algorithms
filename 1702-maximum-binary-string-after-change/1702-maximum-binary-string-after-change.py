class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        
        #find first 0 than shift all zeors from the right into it and flip all 0 pairs into 10s to shift the only zero as far as possible
            
        if '0' not in binary:
            return binary
        
        res = ''
        idx = binary.find('0')
        countZ = binary.count('0')
        
        for i in range(idx):
            res += '1'
        
        while countZ >= 2:
            res += '1'
            countZ -=1
        
        
        res += '0'
        
        for i in range(len(binary) - len(res)):
            res += '1'
        
        
        return res
            
                