class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        
        #coordinates.sort()
        
        #1,2 = 3 #adjust the 1 or adjust the 2 to make 5
        #1001
        #0001
        #0010
        
        #0000
        #0001
        #1000
        
        #
        #1010
        
        
        #0001
        #1000
        
        #1001 5 + 2 find 2"
        
        
        #1 + 2 = 3
        #0001
        #0010
        #1001
        
        #we need a number with the 2 bit on
        #optional 4 bit is on for 1 or 2 
        #optional 1 bit is off for 1 and 1 bit is on for 2
        
        #0001
        #1000
        
        #0001
        #0001 
        
        #= 5
        
        #0010
        #1011
        
        #0001
        #0010 #we cant place a bit if k does not have it or x does not have it
    
        #0010
        #
        
        
        #0001
        #1001
        
        #1000
        
        #0010
        #0011
        
        #any bits not in k must be turned off always
        
        q = []
        
        @cache
        def findMatches(i,x1,x):
            
            if i > 7:
                q.append(x1)
                return q
            
            if x & (1 << i) > 0 and k & (1 << i) == 0:
                findMatches(i+1, x1 ^ (1 << i),x)
            
            elif k & (1 << i) > 0:
                findMatches(i+1, x1,x)
                findMatches(i+1, x1 ^ (1 << i),x)
            
            else:
                findMatches(i+1, x1, x)
                findMatches(i+1, x1 ^ (1 << i),x)
                  
            return q
        
        hmap = Counter()

        #38 + 26
        #38 + 35
        #0 + 35
        #0 + 35
        
        #0011011
        #1011111
        #0111101
        
        #100110
        ans = 0
        for x1,y1 in coordinates:
        
            for val in range(k+1):
                
                y2 = (k - val) ^ y1 
                ans += hmap[(x1 ^ val, y2)]

            hmap[(x1,y1)] +=1

        return ans
