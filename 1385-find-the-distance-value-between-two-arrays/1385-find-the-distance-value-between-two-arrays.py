class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        arr2.sort()

        
        
        def binSearch(e):
            
            l,r = 0, len(arr2) -1
            
            
            
            while l <= r:
                
                
                curr = (l+r) // 2
                
                
                val = e - arr2[curr]
                if val <= d and val >= -d:
                    return True
                
                
                elif val < -d:
                    r = curr -1
                    
                else:
                    l = curr +1
                    
            
            return False
        
        res = 0
        for num in arr1:
            
            
            if not binSearch(num):
                res +=1
                
        return res
                    