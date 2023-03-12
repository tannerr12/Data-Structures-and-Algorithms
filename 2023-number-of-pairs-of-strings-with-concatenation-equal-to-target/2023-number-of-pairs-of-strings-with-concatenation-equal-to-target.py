class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        
        res = 0
        
        hmap = defaultdict(int)
        for i in range(len(nums)):
            hmap[nums[i]] += 1
        
            
        for key,val in hmap.items():
            
            if len(key) >= len(target) or target[:len(key)] != key:
                continue
            
            tar = target[len(key):]
            if tar not in hmap:
                continue
            v1 = hmap[tar]
            
            if tar == key:
                res += val * (val-1)
                continue
            
            res += val * v1
        
        return res