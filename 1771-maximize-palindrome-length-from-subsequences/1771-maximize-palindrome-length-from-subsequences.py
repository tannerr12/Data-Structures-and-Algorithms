class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:

  
        word = word1 + word2
    
        @cache
        def LCS(i,j):
            
            if i > j:
                return 0

            res = float('-inf')

            #take current since i == j
            if word[i] == word[j]:
                res = max(res, LCS(i+1,j-1) + 1 + (j > i))

            #increase i
            res = max(res, LCS(i+1, j))          

            #increase j
            res = max(res, LCS(i, j-1))


            return res
        
        ans = 0
        mp = {}
        
        for i in range(len(word1)):
            if word1[i] not in mp:
                mp[word1[i]] = i
        
        
        for i in range(len(word2) -1, -1 , -1):
            
            if word2[i] in mp:
                ans = max(ans,LCS(mp[word2[i]] +1, len(word1) + i - 1) + 2)
                del mp[word2[i]]
        
        return ans
            
            
            
        ans = LCS(0, len(word) -1,False)
        return ans if ans != float('-inf') else 0