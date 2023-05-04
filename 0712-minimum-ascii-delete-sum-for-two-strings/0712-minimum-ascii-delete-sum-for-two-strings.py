class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        #simplify the problem first
        st1 = ''
        st2 = ''
        res = 0
        
        total = 0
        for v1 in s1:
            total += ord(v1)
        for v2 in s2:
            total += ord(v2)
            
        c1 = Counter(s1)
        c2 = Counter(s2)
        prefix1 = [0]
        prefix2 = [0]
        #rebuild words
        for v1 in s1:
            total += ord(v1)
            if v1 in c2:
                st1 += v1
            else:
                res += ord(v1)
        for v2 in s2:
            total += ord(v2)
            if v2 in c1:
                st2 += v2
            else:
                res += ord(v2)
        
        for v1 in st1:
            prefix1.append(prefix1[-1] + ord(v1))
        for v2 in st2:
            prefix2.append(prefix2[-1] + ord(v2))
                
        if st1 == st2:
            return res
        
        #build next list
        #mp2 = {}
        
        @cache
        def dfs(i, j):
            nonlocal st1,st2
            
            if i >= len(st1) or j >= len(st2):
                if i < len(st1):
                    return (prefix1[-1] - prefix1[i])
                elif j < len(st2):
                    return (prefix2[-1] - prefix2[j])
                return 0
            
            res = float('inf')
            
            
            #take i 
            if st1[i] == st2[j]:
                res = min(res, dfs(i+1, j+1))
            else:
                #skip i
                res = min(res, dfs(i+1, j) + ord(st1[i]))
                #skip j     
                res = min(res, dfs(i,j+1) + ord(st2[j]))   

            return res
        
        

        return dfs(0,0) + res 
