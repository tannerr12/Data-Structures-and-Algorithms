class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        mp = defaultdict(list)
        
        g = gcd(len(arr), k)
        
        for i in range(len(arr)):
            
            mp[i % g].append(arr[i])
            
            
        res = 0
        for key,val in mp.items():
        
            mp[key].sort()
            
            mid = mp[key][len(mp[key]) // 2]
            
            total = 0
            
            for i in range(len(mp[key])):
                
                total += abs(mid - mp[key][i])
            
            res += total
            
        
        
        return res
            