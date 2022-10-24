class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        idx = -1
        l,r = 0,len(arr)-1
        
        
        while l<= r:
            
            
            curr = (l+r)// 2
            
            
            
            if arr[curr] == x:
                idx = curr
                break
            
            elif arr[curr] > x:
                r = curr -1
                
            
            else:
                l = curr +1
                
        
        
        if l != 0:
            l -=1
        if idx == -1:
            idx = l
        
        
        print(idx)
        
        l,r = idx,idx +1
        
        res = []
        while k != 0:
            
            if l == r:
                res.append(arr[idx])
                l-=1
                r+=1
                k-=1
                
 
            elif l >= 0 and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -=1
                
                else:
                    res.append(arr[r])
                    r+=1
                
                k-=1
            elif l >= 0:
                res.append(arr[l])
                l-=1
                k-=1
                
            elif r < len(arr):
                res.append(arr[r])
                r +=1
                k-=1
                
            else:
                break
                
        
        res.sort()
        return res
                
            