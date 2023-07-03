class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        squares = set()
        
        x = 0
        
        while x * x <= 10 ** 9:
            
            squares.add(x*x)
            x +=1
        
        #print(squares)
        
        seqSet = set()
        @cache
        def dfs(mask,last,seq):
            
            if mask == (2 ** len(nums)) -1:
                seqSet.add(seq)
                return
            
            
            for i in range(len(nums)):
                if mask & (1 << i) > 0:
                    continue
                if last == -1 or nums[i] + last in squares:
                    dfs(mask | (1 << i), nums[i], seq + str(nums[i]))
            
            return
        
        dfs(0,-1,'')
        
        return len(seqSet)
            