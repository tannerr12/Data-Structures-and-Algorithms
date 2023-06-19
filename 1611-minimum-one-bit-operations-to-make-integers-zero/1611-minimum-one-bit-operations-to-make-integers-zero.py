class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @cache
        def dfs(num):
            if num == '1':
                return 1
            elif num == '0':
                return 0
            
            res = 0
            
            if num[0] == '1':
                res = helper(num[1:]) + 1 + dfs('1' + '0' * (len(num) -2))
            else:
                res = dfs(num[1:])
            
            return res
            
        @cache
        def helper(num):
           
            if num == '1':
                return 0
            elif num == '0':
                return 1
            
            res = 0
            
            if num[0] == '0':
                res = helper(num[1:]) + 1 + dfs('1' + '0' * (len(num) -2))
            else:
                res = dfs(num[1:])
            
            return res
        
        b = bin(n)[2:]
        return dfs(b)
            
            