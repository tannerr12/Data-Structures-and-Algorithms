class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        c = Counter()
        
        for w in words:
            count = Counter(w)
            
            for key,val in count.items():
                c[key] += val
        
        
        #print(c)
        evens = 0
        odds = 0
        for key,val in c.items():
            if val % 2:
                odds += 1
            
            evens += val // 2
            
        
        words.sort(key=lambda x:(len(x)))
        
        res = 0
        for w in words:
            if len(w) % 2 and odds and evens >= len(w) // 2:
                odds -= 1
                evens -= len(w) // 2
                res += 1
            
            elif evens >= len(w) // 2:
                evens -= len(w) // 2
                res += 1
        
        return res
                
                
                
            
            
            