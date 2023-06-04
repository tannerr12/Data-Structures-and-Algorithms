class Solution:
    def sortArray(self, nums: List[int]) -> int:
        n = nums.copy()
        oup = 0
        idxMp = defaultdict(int)
        oupMp = defaultdict(int)
        for i,v in enumerate(nums):
            idxMp[v] = i
            if v != i and v != 0:
                oup +=1
                oupMp[v] = i
        count = 0
        while n[0] != 0 or oup > 0:
            
            if n[0] == 0 and oup > 0:
                pos = 0
                num = 0
                for key in oupMp:
                    num = key
                    break
                pos = idxMp[0]
                target = idxMp[num]

                idxMp[0],idxMp[num] = idxMp[num],idxMp[0]

                n[pos],n[target] = n[target], n[pos]
               
                count +=1
                continue
                
                    
            pos = idxMp[0]
            target = idxMp[pos]
            
            idxMp[0],idxMp[pos] = idxMp[pos],idxMp[0]
            
            n[pos],n[target] = n[target], n[pos]
            del oupMp[pos]
            count +=1
            oup -=1
        
        res = float('inf')
 
        res = min(res, count)
        oup = 0
        idxMp = defaultdict(int)
        oupMp = defaultdict(int)
        for i,v in enumerate(nums):
            idxMp[v] = i
            if v != i+1 and v != 0:
                oup +=1
                oupMp[v] = i
        n = nums.copy()
        count = 0
        
        while n[-1] != 0 or oup > 0:
            if n[-1] == 0 and oup > 0:
                pos = 0
                num = 0
                for key in oupMp:
                    num = key
                    break
                pos = idxMp[0]
                target = idxMp[num]

                idxMp[0],idxMp[num] = idxMp[num],idxMp[0]

                n[pos],n[target] = n[target], n[pos]
               
                count +=1
                continue
                
            pos = idxMp[0]
            target = idxMp[pos+1]
            
            idxMp[0],idxMp[pos+1] = idxMp[pos+1],idxMp[0]
            
            n[pos],n[target] = n[target], n[pos]
            del oupMp[pos+1]
            count +=1
            oup -=1
        
       
        res = min(res, count)
        
        
            
        return res
        
            
            
            