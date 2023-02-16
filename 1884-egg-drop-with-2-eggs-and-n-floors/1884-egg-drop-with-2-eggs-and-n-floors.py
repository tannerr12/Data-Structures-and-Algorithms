class Solution:
    def twoEggDrop(self, n: int) -> int:
        #math problem... possible with top down
        
        
        @cache
        def dp(floor,eggs):
            
            if eggs == 1 or floor < 1:
                return floor
            
            res = float('inf')
            for tryFloors in range(1, floor +1):
                # egg broke lets add all of the rest of the floors to solve for 1 egg
                # of egg did not break lets continue but add 1 drop
                res = min(res, 1 + max(dp(tryFloors-1,eggs-1), dp(floor - tryFloors, eggs)))
            
            return res
        
        
        return dp(n,2)
                