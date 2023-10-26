class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        diffProf = []
        
        for x,y in zip(difficulty, profit):
            diffProf.append((x,y))
        worker.sort()
        diffProf.sort()
        
        idx = 0
        res = 0
        best = 0
        for i in range(len(worker)):
            
            while idx < len(diffProf) and diffProf[idx][0] <= worker[i]:
                best = max(best, diffProf[idx][1])
                idx +=1
            
            res += best
        
        
        return res