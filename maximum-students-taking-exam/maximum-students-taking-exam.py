class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        #great question for bit states you can use each row as a bitstate and use << and >> to check left and right compare
        
        m = len(seats)
        n = len(seats[0])
        
        validPos = [0] * m
        
        for i in range(m):
            for j in range(n):
                #create an array of bitmasks and if there is a non broken seat set the bit to 1 else 0
                validPos[i] |= (1 << j) if seats[i][j] == '.' else 0 
        
        
        #hamming method to count bits
        def bit_count(n):
            count = 0
            while n:
                n&= n-1
                count += 1
            
            return count
        
      
        @cache
        def backTrack(takenRows, currRow):
            # print(count, takenRows, currRows, rowIdx)
            if currRow == m:
                return 0
            res = 0
            #loop over each rows state
            for state in range(1<<n):
            
                #using << 1 we can shift all of the chairs to the left and put both states overtop
                #of eachother and verify that none of them line up
                #state & valid check will check if the chairs above line up with the current state
                #state & state << 1 check if any chairs are directly next to eachother
                #100011
                #100011 & == 100011
                #011001
                #000101 << 1 = 001010 & = 001000 so invalid 
                if (state & validPos[currRow] == state) and (state & (state<<1) == 0):
                    #shift takenRows to the left and compare it against our current state
                    #same idea as above and current state will be passed in as takenRows in the next call
                    # we also check shifting state to the left by 1 to check left diagnal and right diagnal
                    if (takenRows<<1) & state == 0 and (state<<1) & takenRows == 0:
                        #we can count how many bits we turned on and add it to our total
                        res = max(res, bit_count(state) + backTrack(state, currRow+1))
            return res
        
        return backTrack(0, 0)
            
            
            