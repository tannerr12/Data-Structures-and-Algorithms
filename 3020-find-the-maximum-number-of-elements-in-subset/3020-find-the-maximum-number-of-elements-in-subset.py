class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mp = Counter(nums)
        
        s = set(nums)
        ls = list(s)
        
        @cache
        def check(num):
            if num == 1:
                return mp[num] - (mp[num] % 2 == 0)
            pw = 1
            newnum = num
            size = 0
            while mp[newnum] >= 2:
                pw *=2
                newnum = pow(num, pw)
                size += 2
            
            return size + 1 if mp[newnum] == 1 else size - 1
            
        
        res = 0
        for i in range(len(ls)):
            res = max(res, check(ls[i]))
            
    
        
        return res