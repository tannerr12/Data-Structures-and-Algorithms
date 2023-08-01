class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = []
        
        for i in range(len(requests)):
            start, end = requests[i][0], requests[i][1]
            arr.append((start, 1))
            arr.append((end + 1, -1))
        
        
        arr.sort()
        
        pos = [0] * len(nums)
        
        idx = 0
        total = 0
        for i in range(len(nums)):
            
            while idx < len(arr) and arr[idx][0] == i:
                total += arr[idx][1]
                idx +=1
            pos[i] = total
        
      #  print(pos)
        MOD = 10 **9 + 7
        pos.sort()
        nums.sort()
        res = 0
        for x,y in zip(pos,nums):
            res += x * y
            res %= MOD
            
        return res
        
        
            