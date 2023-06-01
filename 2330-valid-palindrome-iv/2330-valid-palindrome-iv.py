class Solution:
    def makePalindrome(self, s: str) -> bool:
        count = 0
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                count +=1
        return count <= 2