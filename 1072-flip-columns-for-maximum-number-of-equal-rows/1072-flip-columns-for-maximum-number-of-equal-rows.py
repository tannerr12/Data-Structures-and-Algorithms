class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        #create a map of compliments
        mp = defaultdict(int)
        
        #take this example
        '''
        000
        001
        110
        
        The idea is we will try to make all of the rows 000
        if it starts with a 0 dont flip anything but if it 
        starts with a 1 we will want flip everything
        
        000 -> 000
        001 -> 001
        110 -> 001
        
        as we can see here 110 and 001 are exact opposties 
        in terms of bits which means they fit together when flipped
        since we turned them both to their 0 compliments they both become 
        001 so the idea is we want to return the compliment that occurs the most often
        when since that will give us our best result
        
        '''
        
        for r in matrix:
            
            s = ''
            compliment = False
            
            if r[0] == 1:
                compliment = True
            
            for val in r:
                
                if compliment:
                    s += str(val ^ 1)
                else:
                    s += str(val)
                    
            
            mp[s] +=1
        
        
        return max(mp.values())
                