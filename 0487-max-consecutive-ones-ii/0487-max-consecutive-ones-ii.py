class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        zeroes, res = 0,0
        
        
        s = ''.join(str(n) for n in nums)
        
        arr = s.split('0')
        
        #print(arr)
        
        for i in range(len(arr) -1):
            
            res = max(res, len(arr[i]) + len(arr[i+1]) +1)
        
        
        
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return len(arr[0])
        return res