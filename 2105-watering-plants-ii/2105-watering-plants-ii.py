class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        res = 0
        
        i, j = 0, len(plants) -1
        cura,curb = capacityA, capacityB
        while i <= j:
            
            if i != j:
                if plants[i] > cura:
                    cura = capacityA - plants[i]
                    res += 1
                else:
                    cura -= plants[i]
                
                
                if plants[j] > curb:
                    curb = capacityB - plants[j]
                    res += 1
                else:
                    curb -= plants[j]
            
            else:
                if cura >= plants[i] or curb >= plants[i]:
                    return res
                else:
                    return res + 1
            i += 1
            j -= 1
            
        
        return res