class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        
        heap = []
        
        for i,v in enumerate(nums):
            heap.append([v,i])
            
        heap.sort()

        res = 0
        n = len(nums) 
    
        for i in range(1,n):
            
            if heap[i][1] < heap[i-1][1]:
                res += n - i
                
        
        return res + len(nums)
        
