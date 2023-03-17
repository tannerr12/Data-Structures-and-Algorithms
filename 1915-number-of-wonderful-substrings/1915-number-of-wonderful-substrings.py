class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
            # 00
        #01 # 01
        #10 # 11
        #01 # 10
        #01 # 11
        
        #use bitmasks to keep track of odd sums and ^ prefix ranges to check if valid
        
        
        """
        prefix = [0]
        
        for i in range(len(word)):
            
            
            ch = ord(word[i]) - ord('a')
            prefix.append(prefix[-1] ^ (1 << ch))
        """
        #print(prefix)
        
        #go right to left and keep a count of times we see the bitmask
        #also we can go through a - j for each bitmask and count the times a 1 bit diff occurs after this point
        
        mp = defaultdict(int)
        mp[0] +=1
        res = 0
        bit = 0
        for i in range(len(word) -1,-1,-1):    
            ch = ord(word[i]) - ord('a')
            bit ^= (1 << ch)
            res += mp[bit]
    
            for j in range(10):
                flip = bit ^ (1 << j)
                res += mp[flip]
                
            mp[bit] +=1
        
        
        return res