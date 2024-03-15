class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        #aacecaaa
        #aaacecaaa
        #aaacecaaaaacecaaa
        #aaacecaaaacecaaa
        
        #can always be solved by doubling the input
        #every palindorne answer will be odd unless the input is a palindrone
        #every palindrone needs a center element given this if the left side is a sub of the right we can always fill in
        #the right side must be >= to the left side since we cannot extend the right
        
        #[1,2,3] [4] [3,2,1,4,5,6] = 3 we have the prefix left that matches the revered prefix right the middle element is ignored
        #if the left did not match the right we can say its impossible
        
        #how can we efficiently build the left and right so they are easily comparable?
        
        ns = s + '#' + s[::-1]
        
        #print(ns)
        
        i, j = 0,1
        lcs = [0] * len(ns)
        while j < len(ns):
            
            if ns[i] == ns[j]:
                lcs[j] = i+1
                i+=1
                j+=1
                
            else:
                
                if i == 0:
                    j+=1
                else:
                    i = lcs[i-1]
            
        
        
        return s[i:][::-1] + s
            