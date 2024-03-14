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
        if s == s[::-1]:
            return s
        #"abbacd"
        #"dcabbacd"
        left = []
        
        right = list(s)[::-1]
        
        #print(left, right)
        res = len(s) -1
        for i in range(len(s) // 2):
            right.pop()
            
            if right[-len(left):] == left:
                res = min(res, len(right) - len(left))
            
            left.append(s[i])
        
        
        left = []
        
        right = list(s)[::-1]
        
        for i in range(len(s) // 2):
            right.pop()
            left.append(s[i])
            if right[-len(left):] == left:
                res = min(res, len(right) - len(left))
                

        return s[::-1][:res] + s
            