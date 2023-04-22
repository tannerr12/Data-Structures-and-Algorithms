class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n,m = len(s1),len(s2)

        res = '' 
        indicies = collections.defaultdict(list)
        for i in range(n):
            indicies[s1[i]].append(i)
        ind = [0] * m
        
        for start in range(n):
            prev = start -1
            notFound = False
            for j in range(m):
                if s2[j] not in indicies:
                    return ''
                
                cur = indicies[s2[j]]
                while ind[j] < len(cur) and cur[ind[j]] <= prev:
                    ind[j] +=1
                
                if ind[j] == len(cur):
                    return res
                
                prev = cur[ind[j]]
            
            if res == '' or prev-start+1 < len(res):
                res = s1[start:prev+1]
            
        
        
        
        return res
            
        '''
        schar = Counter(s2)
        char = defaultdict(int)
        
        
        l = 0
        res = ''
        size = float('inf')
        for i in range(len(s1)):
            if s1[i] in schar:
                char[s1[i]] += 1
            
            if s1[i] in schar:
                
                valid = True
                for key in schar:
                    if char[key] < schar[key]:
                        valid = False
                        break

                if valid and i-l+1 < size:
                    res = s1[l:i+1]
                    size = i-l+1
                                
                
                
                while l < len(s1) and valid: 
                    valid = True
                    for key in schar:
                        if char[key] < schar[key]:
                            valid = False
                            break
                            
                    if valid and i-l+1 < size:
                        res = s1[l:i+1]
                        size = i-l+1
                        
                    if s1[l] in char:                
                        char[s1[l]] -=1
                        if char[s1[l]] = 
                    l+=1
            
        
        
        valid = True
        for key in schar:
            if char[key] < schar[key]:
                valid = False
                
        if valid and len(s1)-l < size:
            res = s1[l:]
        
        
        return res

        '''
        