class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        
        nums.sort(reverse=True)
        def isGood(mid):
            
            #mult 3
            #x 4
            #y 2
            #diff x - y = 2
            # 10 // y = 5 rem = y * 2 = 4 // diff 
            # 
            
            moves = 0
            for num in nums:
                
                moves += max(0, math.ceil((num - mid * y) / (x - y)))
                
            return moves <= mid
        
        
        l,r = 0, 10 ** 9
        res = float('inf')
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1
        
        return res