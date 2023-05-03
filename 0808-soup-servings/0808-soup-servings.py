class Solution:
    def soupServings(self, n: int) -> float:
        #Edge case that anything >= 4800 ml will always be 1 which greatly simplifies this problem and makes DP possible 
        if n >= 4276:
            return 1
        
        @cache
        def dfs(soup,soup2):
            
            if soup==0 or soup2==0:
                
                if soup == 0 and soup2:
                    return 1
                elif soup == 0 and soup2 == 0:
                    return 0.5
                else:
                    return 0 
            
            res = 0.25 * (dfs(soup - min(soup,100),soup2) + dfs(soup - min(soup, 75),soup2 - min(soup2, 25)) + \
                          dfs(soup - min(soup, 50),soup2 - min(soup2, 50)) + dfs(soup - min(soup,25),soup2 - min(soup2, 75)))
            
            
            return res
        
        
        return dfs(n,n)