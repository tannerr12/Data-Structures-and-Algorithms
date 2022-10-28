class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
        pairs = sorted(pairs, key=lambda x:x[1])
        #heapq.heapify(pairs)
       # print(pairs)
        
        res = 1
        firstVal = pairs[0][1]
        for i in range(1, len(pairs)):
            
            x,y = pairs[i]
            
            
            if x > firstVal:
                firstVal = y
                res +=1
                
        return res