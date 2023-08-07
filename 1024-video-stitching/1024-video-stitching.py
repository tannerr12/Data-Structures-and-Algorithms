class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        clips.sort()
        
        @cache
        def dfs(i,last):
            
            if last >= time:
                return 0
            if i >= len(clips):
                return float('inf')
            
            res = float('inf')
            #take current clip
            if clips[i][0] <= last and clips[i][1] > last:
                res = min(res, dfs(i+1, clips[i][1]) + 1)
            
            #skip clip 
            res = min(res, dfs(i+1, last))
            
            
            return res
        
        val = dfs(0, 0)
        return val if val != float('inf') else -1