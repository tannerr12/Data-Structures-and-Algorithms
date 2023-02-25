class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels = set(jewels)
        
        count = Counter(stones)
        
        
        res = 0
        for char in jewels:
            if char in count:
                res += count[char]
                
        
        return res