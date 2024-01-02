class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        pref = []
        pref.append(0)
        for i in range(len(arr)):
            if arr[i] % 2:
                arr[i] = 1
            else:
                arr[i] = 0
            
            pref.append(pref[-1] + arr[i])
        
        res = 0
        evens = 0
        odds = 0
        for i in range(len(pref)):
            if pref[i] % 2:
                odds += 1
            else:
                evens += 1
            
            if pref[i] % 2:
                res += evens
            else:
                res += odds
            
            res %= MOD
        #print(pref)
        
        return res % MOD
        