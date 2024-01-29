class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        res = 0
        evensN = n // 2
        evensM = m // 2
        oddsN = math.ceil(n / 2)
        oddsM = math.ceil(m / 2)
        
        res += evensN * oddsM
        res += oddsN * evensM
        
        return res
            