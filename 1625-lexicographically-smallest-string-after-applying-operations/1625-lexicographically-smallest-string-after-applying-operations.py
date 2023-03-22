class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        comb = set()
        news = s
        while news not in comb:
            comb.add(news)
            st = ''
            for i in range(len(news)):
                if i % 2:
                    v = int(news[i])
                    v += a 
                    v %= 10
                    st += str(v)
                else:
                    st += news[i]
            
            news = st
        
        if b % 2:
            
            news = s[len(s) - b:] + s[:len(s) - b]
            while news not in comb:
                comb.add(news)
                st = ''
                for i in range(len(news)):
                    if i % 2:
                        v = int(news[i])
                        v += a 
                        v %= 10
                        st += str(v)
                    else:
                        st += news[i]

                news = st
        
        #print(comb)
        res = []
        
        for val in comb:
            st = val
            res.append(val)
            for i in range(len(s) // b):
            
                st = st[len(s) - b:] + st[:-b]
                
                res.append(st)
        
        res.sort()
        
        return res[0]
        """
        
        seen = set()
        def dfs(s):
            
            if s in seen:
                return
            
            seen.add(s)
            #2 options
            #increment all evens
            st = ''
            for i in range(len(s)):
                if i % 2:
                    v = int(s[i])
                    v += a 
                    v %= 10
                    st += str(v)
                else:
                    st += s[i]
            dfs(st)
            #rotate
            st = s[len(s) - b:] + s[:len(s) - b]
            dfs(st)
            
        
        dfs(s)
        
        #print(seen)
        ls = list(seen)
        ls.sort()
        return ls[0]
            
            