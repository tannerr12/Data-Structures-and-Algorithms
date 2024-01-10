class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        start = -1
        end = -1
        for i in range(len(num)):
            
            n = int(num[i])
            if change[n] > n and start == -1:
                start = i
                end = i
            
            elif start != -1 and change[n] < n:
                break
            
            elif start != -1:
                end = i
        
        
        #print(start, end)
        
        if start == -1:
            return num
        
        arr = []
        
        for i in range(len(num)):
            n = int(num[i])
            if i < start or i > end:
                arr.append(num[i])
            else:
                arr.append(str(change[n]))
        
        return ''.join(arr)