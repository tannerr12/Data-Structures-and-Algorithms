class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        
        top = max(damage)
            
        return sum(damage) - min(top,armor) +1