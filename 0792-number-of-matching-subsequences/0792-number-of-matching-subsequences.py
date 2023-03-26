class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        #option 2 binary search an array of arrays of size 26 for next occurance
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
        
        """
        
        mp = defaultdict(list)
        
        for word in words:
            
            mp[word[0]].append(word)
            
            
        res = 0
        for i,s in enumerate(s):
            
            wordls = mp[s]
            mp[s] = []
            for word in wordls:
                
                if len(word) == 1:
                    res +=1
                else:
                    mp[word[1]].append(word[1:])
            
        return res
            