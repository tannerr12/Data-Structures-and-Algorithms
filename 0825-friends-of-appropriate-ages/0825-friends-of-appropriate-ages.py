class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        ages.sort()
        count = Counter(ages)
        mp = defaultdict(int)
        res = 0
        for i in range(len(ages)):
            age = ages[i]
            target = age * 0.5 + 7
            target += 0.1
            #if age > 100 and target < 100:
            #    target = 100
            
            idx = bisect_left(ages,target)
            if idx == i:
                continue
            mp[age] = max(mp[age], i - idx )
            
        
        
        for key,val in mp.items():
            
            mp[key] *= count[key]
        
        return sum(mp.values())
            
        