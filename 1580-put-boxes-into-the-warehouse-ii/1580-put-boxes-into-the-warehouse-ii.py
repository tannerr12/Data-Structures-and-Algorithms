class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        
        boxes.sort()
        bCount = 0
        minheightl = warehouse[0]
        minheightr = warehouse[-1]

        r = len(warehouse)-1
        l = 0
        while boxes and l <= r:
            if len(boxes) == 0:
                break
            minheightl = min(minheightl, warehouse[l])
            minheightr = min(minheightr,warehouse[r])
            
            while boxes and boxes[-1] > minheightl and boxes[-1] > minheightr:
                boxes.pop()
            
            if len(boxes) ==0:
                break
            if minheightl > minheightr:
                l+=1
                bCount +=1
                boxes.pop()
            
            else:
                r -=1
                bCount +=1
                boxes.pop()

        
        
        
        return bCount
        