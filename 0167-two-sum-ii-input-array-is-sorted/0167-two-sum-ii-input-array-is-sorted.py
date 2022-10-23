class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        
        def binarySearch(left,t):
            
            l = left
            r = len(numbers) -1
           
            
            while l <= r:
                
                
                curr = (l+r) //2
                
                if numbers[curr] == t:
                    return curr +1
                
                elif numbers[curr] > t:
                    r  = curr -1
                    
                else:
                    l = curr + 1
            
            
            return -1
                    
        
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t < numbers[i]:
                continue
            rIndex = binarySearch(i +1, t)
            if rIndex != -1:
                return [i+1, rIndex]
            
        