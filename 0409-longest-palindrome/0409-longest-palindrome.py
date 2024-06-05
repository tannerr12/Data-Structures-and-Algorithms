class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictionary = {}
        count = 0
        countExtra = 0
        for i in range(len(s)):
            
            char = s[i]
            
            if char in dictionary:
                dictionary[char] += 1
                
            else:
                dictionary[char] = 1
        
        
        
        for key,value in dictionary.items():
            if value % 2 == 1:
                value = value -1
                countExtra = 1
            count += value
        
        return count + countExtra