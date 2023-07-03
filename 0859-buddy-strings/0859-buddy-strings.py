class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i = 0
        first = -1
        swapped = False
        while i < len(s):
            if s[i] != goal[i] and first == -1:
                first = i
            
            elif s[i] != goal[i] and first != -1 and not swapped:
                if goal[first] == s[i] and s[first] == goal[i]:
                    swapped = True
                else:
                    return False
            
            elif swapped and s[i] != goal[i]:
                return False
            
            i += 1
        
        
        if not swapped and first == -1:
            c = Counter(goal)
            for i in range(len(s)):
                
                if s[i] in c and c[s[i]] > 1 or goal[i] != s[i]:
                    return True
                
        
        return swapped