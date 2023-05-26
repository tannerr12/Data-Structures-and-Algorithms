class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        stack = [heights[-1]]
        res = [0] * len(heights)
        for i in range(len(heights)-2,-1,-1):
            count = 0 
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count +=1
                
            if len(stack) > 0:
                count +=1
            res[i] = count
            stack.append(heights[i])
        
        return res
            