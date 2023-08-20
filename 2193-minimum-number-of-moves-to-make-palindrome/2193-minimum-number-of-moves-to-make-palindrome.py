class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        2 pointers, left and right, such that right = n - left - 1
        i.e., they are equidistant from both ends
        
        in a palindromic arrangement of s, s[left] == s[right]

        if s[left] and s[right] are not equal:
        1. from j = right, check whether there is an element equal to s[left]. 
           decrement j until an equal element is not found
        2. similarly, i = left, check whether there is an element equal to s[right].
           increment i until an equal element is not found
        3. now we need to decide to either move element at left to element at i, or
           element at right to element at j
        4. calculate the cost for both possibilities, (i - left and right - j)
        5. choose the minimum and move those elements by adjacent swaps
        
        
        """
        s = list(s)
        n = len(s)
        count = 0
        
        for left in range(n // 2):
            right = n - left - 1
            if s[left] != s[right]:
                i = left
                j = right
                
                while s[left] != s[j]:
                    j -= 1
                    
                    
                while s[right] != s[i]:
                    i += 1
                    
                    
                if right - j < i - left:
                    count += right - j
                    for x in range(j, right):
                        s[x] = s[x+1]
                else:
                    count += i - left
                    for x in range(i, left, -1):
                        s[x] = s[x-1]
                        
        return count