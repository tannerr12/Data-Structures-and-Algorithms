class Solution:
    def minSwaps(self, s: str) -> int:
     
        ones = s.count('1')
        zeros = len(s) - ones
        
        if len(s) % 2 == 0 and ones != zeros:
            return -1
        elif len(s) % 2 and abs(ones - zeros) != 1:
            return -1
        
        res =0
        cost1,cost2 = 0,0
        
        for i in range(len(s)):
            #010
            if s[i] != str(i%2):
                cost1 +=1
            #101
            else:
                cost2 +=1
            
        if cost1 % 2:
            cost1 = float('inf')
        if cost2 % 2:
            cost2 = float('inf')
            
        res = min(cost1,cost2)
        return res // 2