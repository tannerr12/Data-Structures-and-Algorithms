class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        
        after = 0
        count = 0
        for i in range(len(boxes)):
            if boxes[i] == '1':
                after += i
                count +=1
        
        before = 0
        bcount = 0
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            
            res[i] = after + before
            
            if boxes[i] == '1':
                bcount += 1
                count -=1
            before += bcount
            after -= count
            
        return res