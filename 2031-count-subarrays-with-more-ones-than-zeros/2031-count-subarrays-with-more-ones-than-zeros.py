class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        #res = 0 
        """
        prefix = []
        prefix.append(0)
        for i in range(len(nums)):
            
            if nums[i] == 0:
                prefix.append(prefix[-1] - 1)
            else:
                prefix.append(prefix[-1] + 1)
        
        
       # print(prefix)
        
        c = Counter(prefix)
        #print(c)
        res = 0
        arr = []
        for key,val in sorted(c.items()):
            arr.append([key, val])
        print(arr)
        for i in range(len(prefix) -1):
            
            tar = prefix[i] + 1
            for key,val in c.items():
                if key >= tar:
                    res += val
            
            c[prefix[i]] -=1
            if c[prefix[i]] == 0:
                del c[prefix[i]]
        
        
        return res % MOD
        
        #1 = 1
        #2 = 4 
        #3 = 10
        
        #5 * 6 = 30 // 2 = 15
        #2 * 3 // 2 = 3
        
         #= 12
         
        """
        
        mp = defaultdict(int)
        mp[0] = 1
        
        run, res,total = 0,0,0
        
        for i in nums:
            
            if i > 0:
                run += 1
                #
                total += mp[run-1]
            else:
                run -=1
                total -= mp[run]
            
            res += total
            mp[run] += 1
        
        return res % MOD