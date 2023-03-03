class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        def reverse(l,r):
            
            while l < r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            
        #print(s)
        l = 0
        i = 0
        reverse(0,len(s)-1)
        while i < len(s):
            
            if s[i] == ' ':
                
                reverse(l,i-1)
                l=i+1
            
            i+=1
        
        reverse(l,len(s)-1)
        print(s)