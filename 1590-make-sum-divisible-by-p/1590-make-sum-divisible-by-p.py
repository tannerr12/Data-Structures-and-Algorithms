class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        target = sum(nums) % p
        if target == 0:
            return 0
        
        res = float('inf')
        
        pref = []
        pref.append(0)
        
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])
            pref[-1] %= p
        post = []
        post.append(0)
        
        for i in range(len(nums)-1,-1,-1):
            post.append(post[-1] + nums[i])
            post[-1] %= p
        
        post.reverse()
        
        mp = defaultdict(int)
        for i in range(len(nums)-1,-1,-1):
            
            pst = post[i+1]
            mp[(p - pst) % p] = i
            
            if pref[i] in mp:
                res = min(res, mp[pref[i]] - i + 1)
            
        
   
            
            
        
        return res if res != float('inf') and res != len(nums) else -1
            
        
        