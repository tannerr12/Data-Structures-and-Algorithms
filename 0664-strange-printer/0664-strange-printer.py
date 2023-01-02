class Solution:
    def strangePrinter(self, s: str) -> int:
        
        s = ''.join(a for a, b in zip(s, '#' + s) if a != b)
     
        
        # Track index where each character occurs next for faster lookup
        nxt = {}
        nxtL = list(range(len(s)))
        
        for i, c in enumerate(s):
            if c in nxt:
                nxtL[nxt[c]] = i
            nxt[c] = i
        
        for v in nxt.values():
            nxtL[v] = 10**10
        
        #print(nxt)
        #print(nxtL)
        
        #dp(left,right) is minimum steps to convert a string of repeated s[right]
        # into s[left:right] 
        #note the python half open interval: [left,right]
        @cache
        def dp(left,right):
            
            if left >= right:
                return 0
            
            #desired character on [left]
            if s[right] == s[left]:
                #no cost
                return dp(left + 1, right)
            
            #if our pivot index is left
            #cost of 1
            ans = 1 + dp(left + 1, right)
            
            # this will give us our range because it will tell us
            #when the next same character is 
            pivot = nxtL[left]
            while pivot <= right:
                #split the remaining list into 2 one before pivot and one after
                ans = min(ans, 1 + dp(left + 1, pivot) + dp(pivot + 1, right))
                #get the next occurance of that character by grabbing the pivots pivot
                pivot = nxtL[pivot]
                
            return ans
        
    
        s += '#'
        return dp(0,len(s)-1)
            
            