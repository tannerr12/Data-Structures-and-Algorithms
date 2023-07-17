class Solution:
    def arrangeWords(self, text: str) -> str:
        
        
        arr = text.split(' ')
        for i in range(len(arr)):
            arr[i] = [arr[i].lower(), i]
            
        arr.sort(key=lambda x: (len(x[0]), x[1]))
        
        #print(arr)
        
        res = []
        for i in range(len(arr)):
            if i == 0:
                res.append(arr[i][0][0].upper() + arr[i][0][1:])
            else:
                res.append(arr[i][0])
        
            res.append(' ')
        
        
        res.pop()
        return ''.join(res)