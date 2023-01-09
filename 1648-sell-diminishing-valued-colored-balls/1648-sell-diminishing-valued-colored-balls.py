class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = (10**9) + 7
        inventory.sort()

        
        def isGood(val):
            

            order = 0

            for i in range(len(inventory)):
                if inventory[i] > val: 
                    order += inventory[i] - val
            

            return order > orders
            
        
        
        
        
        l,r = 0, inventory[-1]
        res = 0
        while l<=r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid +1
                l = mid +1
            else:
                r = mid -1
                
        
        

        money = 0
        

        for i in inventory:
            if i > res:

                money += (i + res +1) * (i - res) //2
                orders -= (i - res)
        
        money += res * orders
        return money % MOD
                