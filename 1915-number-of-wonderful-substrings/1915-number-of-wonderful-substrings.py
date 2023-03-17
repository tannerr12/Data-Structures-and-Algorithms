class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        #use bitmasks to keep track of odd sums and ^ suffix ranges to check if valid
        
        #go right to left and keep a count of times we see the bitmask
        #also we can go through a - j for each bitmask and count the times a 1 bit diff occurs after this point
        
        mp = defaultdict(int)
        #the start of our list will be 0 so we increase it by 1
        mp[0] +=1
        res = 0
        bit = 0
        for i in range(len(word) -1,-1,-1):    
            #extract and apply the bit value from character into our suffix
            ch = ord(word[i]) - ord('a')
            bit ^= (1 << ch)
            #if we found an exact match add the number of times this occurance has shown up
            res += mp[bit]
            #A-J so we cycle 10 bits
            for j in range(10):
                #flip each bit in our current suffix and see how many matches we find
                flip = bit ^ (1 << j)
                #add the matches
                res += mp[flip]
            
            #increment this bitmask
            mp[bit] +=1
        
        
        return res