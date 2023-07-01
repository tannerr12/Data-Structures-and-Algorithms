class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        
        for i in range(volume):
            
            left = k-1
            while left >= 0 and heights[left] <= heights[left + 1]:
                left -=1
            
            
            right = k + 1
            while right < len(heights) and heights[right] <= heights[right-1]:
                right += 1
            
            left +=1
            right -=1
            while left+1 < len(heights) and heights[left] == heights[left+1]:
                left += 1
            while right - 1 >= 0 and heights[right] == heights[right -1]:
                right -=1
            
            
            if heights[k] <= heights[left] and heights[k] <= heights[right]:
                heights[k] += 1
            elif heights[left] < heights[k]:
                heights[left] += 1
            else:
                heights[right] += 1
            
            
        
        return heights
                
                