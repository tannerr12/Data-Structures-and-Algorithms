class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        arr_noSquish = []
        for x,y in zip(scores,ages):
            arr_noSquish.append([y,x])
            
        
        arr_noSquish = sorted(arr_noSquish ,key=lambda x: (x[0], x[1]), reverse=True)
        
        arr = []
        last = [-1,-1,-1]
        for x,y in arr_noSquish:
            if [x,y] != last:
                arr.append([x,y,1])
            else:
                arr[-1][2] += 1
            last = [x,y]
            
            
       # print(arr)
        
        
        @cache
        def dfs(i,score):
            
            if i >= len(arr):
                return 0   
            
            res = 0
            #take 
            if arr[i][1] <= score:
                res = max(res,dfs(i + 1, arr[i][1]) + arr[i][1] * arr[i][2])
                
            #dont take
            if arr[i][1] != score:
                res = max(res,dfs(i+1,score))
            
            
            
            return res
        
        
        return dfs(0,float('inf'))
        
        
            
            
            