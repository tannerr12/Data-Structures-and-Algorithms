class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        arr = []
        
        for i in range(len(updates)):
            arr.append((updates[i][0], updates[i][2]))
            arr.append((updates[i][1] + 1, -updates[i][2]))
        
        
        
        arr.sort()
        
        
        ans = [0] * length
        
        idx = 0
        total = 0
        for i in range(length):
            
            while idx < len(arr) and arr[idx][0] == i:
                total += arr[idx][1]
                idx +=1
                
            ans[i] = total
        
        
        return ans