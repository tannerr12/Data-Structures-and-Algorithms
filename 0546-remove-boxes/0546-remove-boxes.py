class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        
        #print(shrunk)
        @cache
        def dfs(l,r,k):
            
            if l > r:
                return 0
            
            while l + 1 <= r and boxes[l] == boxes[l+1]:
                l+=1
                k+=1
            
            res = float('-inf')
            #take all right away
            res = max(res, dfs(l+1, r, 0) + (k+1) * (k+1))
            
            for m in range(l+1, r+1):
                
                if boxes[m] == boxes[l]:
                    res = max(res, dfs(l+1, m-1, 0) + dfs(m, r, k+1))
            
            return res
            
        
        return dfs(0, len(boxes) - 1, 0)
