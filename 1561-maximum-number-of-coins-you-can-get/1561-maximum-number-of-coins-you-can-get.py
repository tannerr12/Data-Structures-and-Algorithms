class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        q = deque()
        
        for p in piles:
            q.append(p)
            
        
        res = 0
        while q:
            
            Alice = q.pop()
            Me = q.pop()
            Bob = q.popleft()
            
            res += Me
        
        
        
        return res
            