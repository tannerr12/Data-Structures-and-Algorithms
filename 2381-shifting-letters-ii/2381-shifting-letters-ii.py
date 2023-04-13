class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        arr = []
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        for st,e,d in shifts:
            
            if d == 0:
                arr.append([st,-1])
                arr.append([e+1,+1])
            else:
                arr.append([st,1])
                arr.append([e+1,-1])
        
        
        arr.sort()
        idx = 0
        count = 0
        res = []
        
        for i in range(len(s)):
            val = s[i]
            while idx < len(arr) and arr[idx][0] <= i:
                count += arr[idx][1]
                idx +=1
            
            cur = ord(val) - ord('a')
            cur += count
            cur %= 26
            
            res.append(alpha[cur])
        
        return ''.join(res)
            
            