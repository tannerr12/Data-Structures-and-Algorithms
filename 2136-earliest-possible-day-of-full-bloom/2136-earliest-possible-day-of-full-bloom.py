class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        
        arr = []
        
        for x,y in zip(plantTime, growTime):
            arr.append([x,y])
            
            
        arr = sorted(arr,key=lambda x: (-x[1], x[0]))
        
        #print(arr)
        
        day =0 
        res = 0
        for x,y in arr:
            day += x
            if res < day + y:
                res = day + y
        
        
        return res