class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        

        l,r = 0, 10 ** 15
        
        while l <= r:
            
            mid = (l+r) //2
            
            calc = mid -1 + mid + mid + 1
            
            if calc == num:
                return [mid-1,mid,mid+1]
                
            elif calc > num:
                r = mid - 1
            
            else:
                l = mid + 1
        
        
        return []
            