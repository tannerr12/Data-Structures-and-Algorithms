class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        banned = set()
        total = 0
        count = 0
        i = 0
        while i < n:
            
            count += 1 
            if count in banned:
                continue
                
            total += count
            banned.add(abs(k - count))
            i += 1
        return total
            