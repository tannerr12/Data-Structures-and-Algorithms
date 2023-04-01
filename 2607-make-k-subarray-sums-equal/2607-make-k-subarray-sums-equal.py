class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        mp = defaultdict(list)
        #gcd is important here to account for k overlapps 2,5,5,7 k = 3 
        #if we try to use k here we will have 3 groups 2 and 7 as well as 5,5 in seperate groups  
        #if we use GCD it will count the overlaps as well since after 5 the next 3 is actually idx = 1 than idx =0 so they should all be in the same group
        #gcd len(arr) and k is 1 here which puts all numbers in the same group
                                                
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
            