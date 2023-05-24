class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        res = 0
        stack = []
        dp = [0] * len(books)
        
        
        
        def dfs(left, i):
            
            if books[i] - (i-left) > 0:
                r = (i - left)
                start = books[i] - (i-(left+1))
                end = books[i]
                s= (start + end) * r //2
            else:
                r = books[i]
                start = 1
                end = books[i]
                s = (end * (end + 1)) //2
               # s = (start + end) * r // 2
            
            dp[i] = s
            dp[i] += dp[left] if left >= 0 else 0

        
        for i, c in enumerate(books):
            
            if c != 0:
                
                while stack and books[stack[-1]] >= books[i] - (i - stack[-1]):
                    stack.pop()
                
                left = stack[-1] if stack else -1
                dfs(left, i)
                res = max(res, dp[i])
                
            
            stack.append(i)
            
        
        return res