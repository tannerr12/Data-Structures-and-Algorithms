class Solution:
    def minSwaps(self, s: str) -> int:
        """
        mask1 = "010"
        mask2 = "101"
        ls = list(s)
        def dfs(i):
            
            if i >= len(ls):
                return 0
            
            val = ls[i-2] + ls[i-1] + ls[i]
            cost1,cost2 = 0,0
            for j in range(3):
                if val[j] != mask1[j]:
                    cost1 += 1
                else:
                    cost2 += 1
            res = float('inf')
            #option 1 flip to 010
            ls[i] = '0' 
            res = min(res,dfs(i+2) + cost1)
            
            #option 2 flip to 101
            ls[i] = '1'
            res = min(res,dfs(i+2) + cost2)
            
            
            return res
        
        
        return dfs(2)
        """
        
        ones = s.count('1')
        zeros = s.count('0')
        
        if len(s) % 2 == 0 and ones != zeros:
            return -1
        
        if len(s) % 2 and abs(ones - zeros) != 1:
            return -1
        
        mask1 = ''
        mask2 = ''
        
        for i in range(len(s)):
            if i % 2:
                mask1 += '0'
                mask2 += '1'
            else:
                mask1 += '1'
                mask2 += '0'
        
        #print(mask1)
        #print(mask2)
        res =0
        cost1,cost2 = 0,0
        
        for i in range(len(s)):
            if s[i] != mask1[i]:
                cost1 +=1
            if s[i] != mask2[i]:
                cost2 +=1
            
        if cost1 % 2:
            cost1 = float('inf')
        if cost2 % 2:
            cost2 = float('inf')
        res = min(cost1,cost2)
        return res // 2