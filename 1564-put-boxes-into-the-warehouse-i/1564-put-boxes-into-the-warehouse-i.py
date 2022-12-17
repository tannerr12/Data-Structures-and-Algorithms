class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        
        
        boxes.sort(reverse=True)
        wPos = 0
        for i in range(len(boxes)):
            if wPos == len(warehouse):
                break
            if boxes[i] <= warehouse[wPos]:
                
                wPos +=1
                
        
        
        return wPos