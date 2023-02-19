class Solution:
    def grayCode(self, n: int) -> List[int]:
        #lenght must be 2**n of size
        res = []
        cur = [0]
        seen = set()
        seen.add(0)
        @cache
        def dfs(num):
            nonlocal res
            if len(cur) == (2**n):
                #count bits
                diff = 0
                for i in range(n):
                    if cur[-1] & (1<<i) > 0:
                        diff+=1
                
                if diff == 1:
                    res = cur.copy()
                return
            elif len(cur) == (2**n):
                return
            
            
            for bit in range(n):

                if num ^ (1<<bit) in seen:
                    if len(cur) != 1:
                        continue
                cur.append(num ^ (1<<bit))
                seen.add(num ^ (1<<bit))
                dfs(num ^ (1 << bit))
                seen.remove(num ^ (1<<bit))
                cur.pop()

        
    
        dfs(0)
        
        return res