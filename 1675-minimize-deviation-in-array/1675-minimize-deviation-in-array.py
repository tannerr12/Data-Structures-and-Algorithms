class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        #Learning reference: https://www.youtube.com/watch?v=boHNFptxo2A&ab_channel=NeetCodeIO
        #the idea here is we keep a min heap and a variable to keep track of the current max value 
        #we start by dividing all of the numbers we can to there lowest value and add them to our heap
        #we will also need to keep track of its original value or if its odd its original value * 2
        #this will allow us to get past the corner case of ex 16 1-> 2 - > 4 -> 8 -> 16 since this is normally not possible
        #but these values need to be concidered.
        #Another thing to notice is odd numbers can only double once ever since the double of an odd is always an even.
        minHeap = []
        maxHeap = 0
        
        for num in nums:
            tmp = num
            #while even get its lowest start
            while num % 2 == 0:
                num //= 2
            #add our start and the original or original * 2
            heappush(minHeap, (num, max(tmp,num * 2)))
            maxHeap = max(maxHeap, num)
            
        
        res = float('inf')
        #if we lose a single value we are no longer checking all of the numbers so we can exit
        while len(minHeap) == len(nums):
            
            val,mx = heappop(minHeap)
            #max vs min
            res = min(res, maxHeap - val)
            # if it is less than our original or original * 2 we can push the * 2 value onto the heap and update the maxheap
            if mx > val:
                
                heappush(minHeap, (val * 2, mx))
                maxHeap = max(maxHeap, val*2)
        return res
        
            

            