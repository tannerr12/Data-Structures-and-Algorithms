class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        c = Counter(s)
        
        ans = []
        
        if c["1"] == 0:
            return s
        
        ans.append("1")
        c["1"] -=1
        zero = ["0"] * c["0"]
        
        one = ["1"] * c["1"]
        
        ans = ans + zero + one
        
        ans.reverse()
        return ''.join(ans)
        