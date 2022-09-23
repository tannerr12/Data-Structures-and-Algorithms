class Solution:
    def reverseWords(self, s: str) -> str:
        
        q = deque()
        arr = s.split(' ')
        print(arr)
        
        
        for i in range(len(arr)):
            val = arr[i]
            if val == '':
                continue
            
            q.appendleft(val)
        
        
        
        return ' '.join(q)