class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i,temp,total):
            if total > target:
                return
            if total == target:
                res.append(temp.copy())
                return
            if i >= len(candidates):
                return
            
            temp.append(candidates[i])
            total += candidates[i]
            backtrack(i +1, temp,total)
            total -= candidates[i]
            temp.pop()
            
            while i < len(candidates) -1 and candidates[i] == candidates[i+1]:
                
                i+=1
            
            
            backtrack(i+1, temp,total)
            
            
        
        backtrack(0,[],0)
        return res
            
                