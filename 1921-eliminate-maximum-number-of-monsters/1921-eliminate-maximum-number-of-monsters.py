class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        newArr = []
        
        for a,b in zip(dist,speed):
            
            newArr.append(math.ceil(a/b))
            
        
        #print(newArr)
        
        newArr.sort()
        
        #mn = 0 
        
        for i in range(len(newArr)):
            
            if newArr[i] <= i:
                return i
        
        
        return len(newArr)