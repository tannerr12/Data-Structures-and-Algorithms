class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        
        jumpPath1 = 0
        
        jumpPath2 = 0
        prev1 = stones[0]
        prev2 = stones[0]
        for i in range(0,len(stones),1):
            if i == len(stones) -1:
                jumpPath1 = max(jumpPath1, abs(stones[i] - prev1))
                prev1 = stones[i]
                jumpPath2 = max(jumpPath2, abs(stones[i] - prev2))
                prev2 = stones[i]
            elif i % 2 == 0:
                jumpPath1 = max(jumpPath1, abs(stones[i] - prev1))
                prev1 = stones[i]
            else:
                jumpPath2 = max(jumpPath2, abs(stones[i] - prev2))
                prev2 = stones[i]
            
                       
        
        
        return max(jumpPath1,jumpPath2)
        
        
        
    
            