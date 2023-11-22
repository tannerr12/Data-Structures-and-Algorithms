class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        def checkPath(i,j):
            
            if i < 0 or j < 0 or j >= bestj:
                return False
            
            return True
        
        bestj = 0
        count = 0
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append((i+j, -i, nums[i][j]))
                
        
        arr.sort()
        #print(arr)
        newArr = []
        for i in range(len(arr)):
            newArr.append(arr[i][2])
        
        return newArr
        
        '''
        starti, startj = 0,0
        
        while len(arr) < count:
            
            i,j = starti,startj
            
            
            while checkPath(i,j):
                
                
                if len(nums[i]) > j:
                    arr.append(nums[i][j])
                     
                i-=1
                j+=1
            
            
            
            if starti < len(nums)-1:
                starti +=1
            
            elif startj < bestj - 1:
                startj +=1
            
            else:
                return arr
        '''