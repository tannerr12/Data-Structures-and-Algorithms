class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
        arr = [1] * n
        MOD = 10 ** 9 + 7
        for i in range(k):
            total = 1
            for j in range(1,len(arr)):
                total += arr[j]
                total %= MOD
                arr[j] = total
                arr[j] %= MOD
        
        
        return arr[-1]