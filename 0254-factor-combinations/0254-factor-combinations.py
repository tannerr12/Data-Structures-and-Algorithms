class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        arr = []
        res = []
        
        
        @cache
        def dfs(n):
            lst = []
            if n == 1:
                return
            i =2
            while i <= sqrt(n):
                if n % i == 0:
                    subLst = dfs(n//i)
                    for l in subLst:
                        tmp = l.copy()
                        tmp.append(i)
                        lst.append(tmp)
                    lst.append([i, n//i])
                
    
                i += 1 
       
            ret = []
            
            hs = set()
            for e in lst:
                e.sort()
                st = "".join([str(el) for el in e])
                if st not in hs:
                    hs.add(st)
                    ret.append(e)
            
            return ret
            
        return dfs(n)
        
    
            