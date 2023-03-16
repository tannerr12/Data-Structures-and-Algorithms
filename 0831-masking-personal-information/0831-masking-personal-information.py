class Solution:
    def maskPII(self, s: str) -> str:
        #nothing to the question its just super tedious
        #first figure out if it is an email or a phone #
        email = False
        if '@' in s:
            email = True
            
        newst = ''
        if email:
            
            idx = s.find('@')
            
            name = s[:idx]
            
            domain = s[idx + 1:]
            
            newst += s[0].lower()
            newst += '*' * 5
            newst += s[idx-1].lower()
            
            newst += '@'
            
            for st in domain:
                
                newst += st.lower()
            
            return newst
            
        else:
            
            ns = ''
            for char in s:
                if char in '()-+ ':
                    continue
                
                ns += char
            
            newst = '-' + ns[len(ns) -4:]
            count = 0
            
            for i in range(len(ns)-5,-1,-1):
                
                if count and count % 3 == 0:
                    newst = '-' + newst
                newst = '*' + newst
                count +=1
            
            if count > 6:
                newst = '+' + newst
            return newst