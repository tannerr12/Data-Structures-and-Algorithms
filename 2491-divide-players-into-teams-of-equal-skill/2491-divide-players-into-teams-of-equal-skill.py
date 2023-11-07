class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2:
            return -1
        
        skill.sort()
        
        #print(skill)
                
        #[1, 2, 3, 3, 4, 5]
        
        i,j = 0, len(skill)-1
        res = 0
        base = skill[0] + skill[-1]
        while i < j:
            
            if skill[i] + skill[j] != base:
                return -1
            res += (skill[i] * skill[j])
            i += 1
            j -= 1
        
        return res