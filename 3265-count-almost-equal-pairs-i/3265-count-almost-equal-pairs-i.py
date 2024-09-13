class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        mp = defaultdict(set)
        
        for i in range(len(nums)):
            
            num = nums[i]
            num = str(num)
            
            
            mp[i].add(num.zfill(7))
            
            for j in range(len(num)):
                for k in range(j + 1, len(num)):
                    
                    #if num[j] != num[k]:
                    w = num[:j] + num[k] + num[j+1:k] + num[j] + num[k+1:]
                    w = w.zfill(7)
                    mp[i].add(w)
            
            
        #print(mp)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num = nums[i]
                num = str(num)
                num = num.zfill(7)
                if num in mp[j]:
                    ans += 1
                 

                
        return ans
                             