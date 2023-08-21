class Solution:
    def countOfAtoms(self, formula: str) -> str:
        #countMp = defaultdict(int)
        def dfs(s,countMp):
            curr = ''
            count = 0
            i = 0
            while i < len(s):
                
                if s[i].isalpha():
                    if s[i].islower():
                        curr += s[i]
                    else:    
                        if count == 0:
                            count = 1
                        countMp[curr] += count
                        curr = s[i]
                        count = 0
                elif s[i].isnumeric():
                    count *= 10 
                    count += int(s[i])
            
                else:
                    #countMp[curr] += count
                    stack = ['(']
                    start = i
                    i+=1
                    while stack:
                        if s[i] == '(':
                            stack.append('(')
                        elif s[i] == ')':
                            stack.pop()
                            
                        i+=1
                    
                    end = i-1
                    num = 0
                    
                    while i < len(s) and s[i].isnumeric():
                        num *= 10
                        num += int(s[i])
                        i+=1
                       
                    
                        
                    mp = dfs(s[start+1:end], defaultdict(int))
                    for key,val in mp.items():
                        if num > 0:
                            mp[key] = val * num
                        countMp[key] += mp[key]
                    
                
                    i-=1
                i+=1
            
            if count == 0:
                count = 1
            countMp[curr] += count
            count = 0

            return countMp
            
        countMp = dfs(formula,defaultdict(int))
        
        #print(countMp)
        res = ''
        for key in sorted(countMp):
            if key == '':
                continue
            res += key
            if countMp[key] > 1:
                res += str(countMp[key])
        
        return res