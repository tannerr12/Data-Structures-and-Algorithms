class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        
                
        def checkDist(x, y):
            
            ch1 = ord(x) - ord('a')
            ch2 = ord(y) - ord('a')
            
            if ch2 >= ch1:
                return ch2 - ch1
            else:
                return 26 - ch1 + ch2
    
        arr = [0] * len(s)
        
        for i in range(len(s)):
            arr[i] = checkDist(s[i], t[i])
            
        #print(arr)
        
        mx = k // 26
        
        count = [0] * 25
        
        for i in range(len(count)):
            
            count[i] += mx + ((k % 26) > i)
        
        #print(count)
        arr.sort()
        
        
        for i in range(len(arr)):
            if arr[i] > 0:
                if count[arr[i]-1] == 0:
                    return False
                else:
                    count[arr[i]-1] -= 1
        
        return True
        
        
            