from sortedcontainers import SortedList
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
                
        sl = SortedList()
        
        for x,y in flowers:
            sl.add((x,1))
            sl.add((y+1,-1))
        
        
        
        local = 0
        res = []
        val = []
        for x,y in sl:
            local += y
            if res and res[-1] == x:
                res[-1] = x
                val[-1] = local
            else:    
                res.append(x)
                val.append(local)
            
        
        def bin(target):
            
            l,r = 0, len(res) -1
            
            while l <= r:
                
                mid = (l+r)//2
                
                if res[mid] == target:
                    return mid
                elif res[mid] > target:
                    r = mid -1
                else:
                    l = mid +1
            
            return l -1
        #print(sl)
        #print(res)
        #print(val)
        r = []
        for i in persons:
            if i < res[0] or i > res[-1]:
                r.append(0)
                continue
            j = bin(i)
            r.append(val[j])
        
        
        return r
            