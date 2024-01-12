class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        
        @cache
        def dfs(i,money,coupon):
            
            if i >= len(price):
                return 0
            
            res=0
            
            if money >= price[i]:
                #take
                res = max(res, dfs(i+1, money - price[i],coupon) + tastiness[i])
                
            if money >= price[i] // 2 and coupon:
                res = max(res, dfs(i+1, money - price[i] // 2, coupon - 1) + tastiness[i])
            #skip
            res = max(res, dfs(i+1, money, coupon))
            
            return res
        
        
        return dfs(0,maxAmount, maxCoupons)
        