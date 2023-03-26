class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        arr = [[] for i in range(26)]
        for i in range(len(s)):
            v = ord(s[i]) - ord('a')
            arr[v].append(i)
        
       

        res = 0
        for word in words:
            
            j = 0
            idx = 0
            valid = True
            while j < len(word):
                char = word[j]
                v = ord(char) - ord('a')
                if len(arr[v]) == 0:
                    valid = False
                    break
                idx = bisect_left(arr[v],idx)
                j +=1
                if idx >= len(arr[v]):
                    valid = False
                    break
                idx = arr[v][idx] +1
                    
            if valid:
                res +=1
        
        return res