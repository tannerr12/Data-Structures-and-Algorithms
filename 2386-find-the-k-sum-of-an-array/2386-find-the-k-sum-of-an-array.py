class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        best = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                best += nums[i]
                arr.append(nums[i])
            else:
                arr.append(-nums[i])
        
        print(best)
        arr.sort()
        

        results = []
        
        
        #1,2,3,4,10,12
        print(arr)
        
        heap = [[-best, 0]]
        
        for i in range(k):
            
            val, pos = heappop(heap)

            if pos < len(arr):
                
                heappush(heap, [val + arr[pos], pos + 1])
                if pos:
                    heappush(heap, [val - arr[pos-1] + arr[pos], pos+1])
           
        
        
        return -val
            
        

                