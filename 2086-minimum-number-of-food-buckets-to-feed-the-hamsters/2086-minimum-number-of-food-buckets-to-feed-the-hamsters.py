class Solution:
    def minimumBuckets(self, s: str) -> int:
        
        
        #arr = []
        """
        for i in range(len(s)):
            
            back = i -2
            back1 = i-1
            front = i + 2
            front1 = i + 1
            if back >= 0 and s[back] == 'H' and front < len(s) and s[front] == 'H'
        """
        """
        feed = [0] * len(s)
            
        for i in range(1, len(s)):
            
            if s[i-1] == '.' and s[i] == 'H':
                feed[i-1] +=1
        
        for i in range(len(s)-2,-1,-1):
            if s[i+1] == '.' and s[i] == 'H':
                feed[i+1] +=1
        
        """
        #print(feed)
        arr = [0] * len(s)
        res = 0
        for i in range(len(s)):
            if s[i] == 'H':
                if i+1 < len(s) and s[i+1] == '.':
                    if i - 1 >=0 and arr[i-1]:
                        continue
                    arr[i+1] = 1
                elif i-1 >= 0 and s[i-1] == '.':
                    arr[i-1] = 1
                else:
                    return -1
                
        #print(arr)
        return sum(arr)