class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        
        
        def reorder(s):
            count1 = 0
            count2 = 0
            
            for i in range(len(s)):
                count1 = 0
                for j in range(i, len(s)):
                    if s[j] == '1':
                        count1 += 1
                    else:
                        count1 -= 1
                    if count1 == -1:
                        break
                    if count1 == 0:
                        count2 = 0
                        for k in range(j + 1, len(s)):

                            if s[k] == '1':
                                count2 += 1
                            else:
                                count2 -= 1
                            
                            if count2 == -1:
                                break
                            if count2 == 0:
                                new = s[:i] + s[j+1:k+1] + s[i:j+1] + s[k+1:]
                                if new > s:
                                    return new
        
            return s
        
        while True:
            ns = reorder(s)
            if s == ns:
                return ns
            s = ns
        
        