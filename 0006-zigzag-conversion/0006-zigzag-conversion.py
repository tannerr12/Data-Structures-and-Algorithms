class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        arr = collections.defaultdict(list)
        c = 0
        r = numRows -1
        count = 0
        
        while count < len(s):
            for i in range(numRows):
                if count >= len(s):
                    arr[c].append('')
                    continue
                    
                arr[c].append(s[count])
                count +=1
      
            c+=1
            r = numRows-1
            while r >0:
                r-=1
                if r == 0:
                    break
                
                for i in range(numRows):
                    if count >= len(s):
                        arr[c].append("")
                        continue
                    
                    if i == r:
                        arr[c].append(s[count])
                        count +=1
                    else:
                        arr[c].append("")
                c+=1
                        
                    
            #c+=1
        
        st = ''
        i = 0
        while i < numRows:
            for key, item in arr.items():
                st += item[i]
            i+=1
        
        return st