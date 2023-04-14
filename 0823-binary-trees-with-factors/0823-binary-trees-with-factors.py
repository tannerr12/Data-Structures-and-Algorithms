class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        #prime factorization
        #has to be 2 numbers
        MOD = 10 ** 9 + 7
        seen = set(arr)
        arr.sort()
        ans = 0
       
        @cache
        def dfs(num):
            nonlocal ans

            if num == 1:
                return 1
            
            res = 0
            
            #we need to attempt all pairs of prime numbers
            
            for j in range(len(arr)):
                if arr[j] > num:
                    break
                if arr[j] == num:
                    res +=1
                    continue
                if num % arr[j] == 0 and num // arr[j] in seen:
                    res += dfs(num//arr[j]) * dfs(arr[j])
                    
            return res
        
        
        for i,v in enumerate(arr):
            ans += dfs(v)
            ans %= MOD
        
        
        return ans 
        