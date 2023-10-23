class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def isGood(i,mid):
            
            rembug = budget
            for j in range(len(composition[i])):
                rembug -= max(0, ((composition[i][j] * mid) - stock[j]) * cost[j])
                if rembug < 0:
                    return False
                
            return True
        
        ans = 0
        
        for i in range(len(composition)):
            
            l,r = 0, 10**9
            
            while l <= r:
                
                mid = (l+r) // 2
                
                if isGood(i,mid):    
                    ans = max(ans, mid)
                    l = mid + 1 
                else:
                    r = mid - 1
                    
            
            
        
        return ans