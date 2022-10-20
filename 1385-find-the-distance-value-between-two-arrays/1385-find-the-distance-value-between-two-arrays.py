class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        

        n = 0
        for num in arr1:
            found = False
            for num2 in arr2:
                if abs(num - num2) <= d:
                    found = True
                    continue
            
            if found == False:
                n +=1
        
        return n
            