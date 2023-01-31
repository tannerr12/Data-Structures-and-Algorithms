class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 **9 + 7
        res = 1
        
        if len(nums) == 1:
            return nums[0] + k
        
        c = Counter(nums)
        
        nums = []
        
        for key,val in c.items():
            
            heappush(nums, [key,val])
        
        
        while k and nums:
            
            val,mult = heappop(nums)
            pval = val
            if nums:
                dist = (nums[0][0] - val) * mult
                
                if k >= dist:
                    v2,m2 = heappop(nums)
                    m2 += mult
                    heappush(nums,[v2,m2])
                    k-= dist
                else:
                    diff = dist - k
                    level = k // mult
                    val += level
                    right = k - (level * mult)
                    heappush(nums,[val+1,right])
                    heappush(nums,[val,mult - right])
                    k=0
                    
            else:
                    level = k // mult
                    val += level
                    
                    right = k - (level * mult)
                    heappush(nums,[val+1,right])
                    heappush(nums,[val,mult - right])
                    k=0
                    
            
        
        
        while nums:
            
            val,mult = heappop(nums)
            res *= (val ** mult) % MOD
            
        
        return res % MOD
            