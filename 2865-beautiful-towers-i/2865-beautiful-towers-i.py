class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        left = [0] * len(maxHeights)
        right = [0] * len(maxHeights)
        
        
        mono = []
        total = 0
        
        for i in range(len(maxHeights)):
            t = 1
            while mono and maxHeights[i] < mono[-1][0]:
                size, count = mono.pop()
                t += count
                total -= size * count
            
            
            
            total += t * maxHeights[i]
            mono.append((maxHeights[i], t))
            left[i] = total
        
        
        mono = []
        total = 0
        for i in range(len(maxHeights)-1,-1,-1):
            t = 1
            while mono and maxHeights[i] < mono[-1][0]:
                size, count = mono.pop()
                t += count
                total -= size * count
            
            
            
            total += t * maxHeights[i]
            mono.append((maxHeights[i], t))
            right[i] = total
            
                
        
        print(left)
        print(right)
        res = 0
        for i in range(len(maxHeights)):
            res = max(res, left[i] + right[i] - maxHeights[i])
            
        return res