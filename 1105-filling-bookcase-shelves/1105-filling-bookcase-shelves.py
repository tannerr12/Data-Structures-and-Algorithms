class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def dfs(i,ch,sw):
            
            if i >= len(books):
                return ch
            
            res = float('inf')
            #add to current 
            if sw >= books[i][0]:
                res = min(res, dfs(i+1, max(ch,books[i][1]), sw - books[i][0]))
            
            #start a new
            res = min(res, dfs(i+1, books[i][1], shelfWidth - books[i][0]) + ch)
            
            return res
        
        
        return dfs(0,0,shelfWidth)
                
            