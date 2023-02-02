class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        
        
        countAll = Counter(candies)
        
        
        l = 0
        res = 0
        for i,val in enumerate(candies):
            
           
            countAll[val] -=1
            if countAll[val] == 0:
                del countAll[val]
            
            while i-l + 1 > k:
                
            
                if candies[l] not in countAll:
                    countAll[candies[l]] = 1
                else:
                    countAll[candies[l]] +=1
                l +=1
            
            
            if i - l + 1 == k:
                res = max(res, len(countAll))
        
        
        return res
        