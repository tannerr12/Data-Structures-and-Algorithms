class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0] * 32
        
        for i in range(len(candidates)):
            
            for j in range(32):
                if candidates[i]  & (1 << j) != 0:
                    bits[j] +=1
        
        #print(bits)
        
        return max(bits)
   