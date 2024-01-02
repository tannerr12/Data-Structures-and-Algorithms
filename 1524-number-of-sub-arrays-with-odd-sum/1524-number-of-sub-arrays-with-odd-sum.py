class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
            
        res = 0
        evens = 1
        odds = 0
        pref = 0
        for i in range(len(arr)):
            pref += arr[i] % 2
            if pref % 2:
                odds += 1
            else:
                evens += 1
            
            if pref % 2:
                res += evens
            else:
                res += odds
            
            res %= MOD
        #print(pref)
        
        return res % MOD
        