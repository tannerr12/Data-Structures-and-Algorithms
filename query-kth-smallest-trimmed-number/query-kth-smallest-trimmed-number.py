class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        
        def countingSort(pos):
            
            count = [0] * 10
            
            for val,idx in newNums:
                count[(val // pos) % 10] +=1
            
            
            index = 0
            for i, v in enumerate(count):
                count[i] = index
                index += v
            
            
            ls = [0] * len(newNums)
           
            for i,v in enumerate(newNums):
                val = (v[0]//pos) % 10

                ls[count[val]] = [v[0],v[1]]
                count[val] +=1
            
            
            
      
            for i in range(len(newNums)):
                newNums[i] = ls[i]
                

                
            
        
        newNums = []
        m = 0
        charMap = {}
        for i,val in enumerate(nums):
            m = max(m, len(val))
            newNums.append([int(val),i])
  
        size = defaultdict(list)
        
        placeVal = 1
        for i in range(1,m+1):
            
            #perform radix sort 100 times and store output in dictionary
            countingSort(placeVal)
            size[i] = newNums.copy()
            placeVal *= 10   
    
        res = []
        
        for x,y in queries:
            
            res.append(size[y][x-1][1])
        
        return res
        
        