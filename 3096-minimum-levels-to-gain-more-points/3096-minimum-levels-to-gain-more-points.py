class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        zeros = len(possible) - sum(possible)
        ones = sum(possible)
        
        alice = 0
        for i in range(len(possible)-1):
            if possible[i] == 1:
                alice += 1
                ones -= 1
            else:
                alice -= 1
                zeros -= 1
            
            bob = ones - zeros
            
            if alice > bob:
                return i + 1
        
        return -1