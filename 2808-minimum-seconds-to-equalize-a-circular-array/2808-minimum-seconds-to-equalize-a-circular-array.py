class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        
        new = nums + nums
        
        print(new)
        
        dist = defaultdict(int)
        last = defaultdict(int)
        for i in range(len(new)):
            
            if new[i] in last:
                dist[new[i]] = max(i-last[new[i]], dist[new[i]])
                last[new[i]] = i
            else:
                last[new[i]] = i
               
            
        
        #print(dist)
        val = min(dist.values())
        return val // 2
                