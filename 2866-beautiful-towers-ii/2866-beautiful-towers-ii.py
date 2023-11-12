class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        #for each postion we take the current max + the best values from the right + best values from the left 
        
        #we can use a monotonic stack for left to right
        #5,3,4,1,1,
        
        #3,3,4,1
        
        #3,3,1,1
        
        mono = []
      
        
        #for i in range(len(maxHeights) -1, -1, -1):
            
        #    while 
        
        best = [0] * len(maxHeights)
        running = 0
        for i in range(len(maxHeights)):
            c = 1
            while mono and mono[-1][0] > maxHeights[i]:
                
                val,count = mono.pop()
                c += count
                running -= val * count
            
            running += maxHeights[i] * c
            best[i] = running
            
            mono.append((maxHeights[i], c))
        

        
        mono = []
        running = 0
        for i in range(len(maxHeights) -1, -1,-1):
            c = 1
            while mono and mono[-1][0] > maxHeights[i]:
                
                val,count = mono.pop()
                c += count
                running -= val * count
            
            running += maxHeights[i] * (c - 1)
            best[i] += running
            running += maxHeights[i]
            mono.append((maxHeights[i], c))
        
        
        #print(best)
        
        
        return max(best)
        