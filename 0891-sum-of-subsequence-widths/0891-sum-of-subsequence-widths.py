class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        '''
        
        
        The order in initial arrays doesn't matter,
        my first intuition is to sort the array.

        For each number A[i]:

        There are i smaller numbers,
        so there are 2 ^ i sequences in which A[i] is maximum.
        we should do res += A[i] * 2^i

        There are n - i - 1 bigger numbers,
        so there are 2 ^ (n - i - 1) sequences in which A[i] is minimum.
        we should do res -= A[i] * 2^(n - i - 1)

        Done.
        '''
        #all that matters is the fist take and the last take 
        nums.sort()
        
        res = 0
        MOD = 10**9+7
        n = len(nums)
        for i in range(len(nums)):
            #where we are the largest point
            res += (nums[i] * pow(2,i,MOD)) % MOD
            
            res %= MOD
            
            #where we are the smallest point
            res -= (nums[i] * pow(2,n - i - 1,MOD)) % MOD
            
            res %= MOD
        
        return res
        #1,2,3
        
        #2 - 1 * 2**gap
            