class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        arr = []
        skillmap = {}
        for i in range(len(req_skills)):
            skillmap[req_skills[i]] = i
            
        
        for i in range(len(people)):
            mask = 0
            for skill in people[i]:
                mask |= (1 << skillmap[skill])
            
            arr.append(mask)
        
        
        bitmask = 2 ** len(req_skills)
        bitmask -= 1
        ans = []
        gtotal = float('inf')
        copy = []
        
        @cache
        def dfs(i,m,total):
            nonlocal bitmask,gtotal,ans,copy
            if i >= len(arr) or m == bitmask:
                if m == bitmask:
                    if total < gtotal:
                        gtotal = total
                        copy = ans.copy()
                    return total
                
                return float('inf')
            
            
            res = float('inf')
            
            #dont take
            res = min(res,dfs(i+1, m,total))
            
            if arr[i] > 0 and arr[i] & m != arr[i]:
                ans.append(i)
                #take
                res = min(res,dfs(i+1, m | arr[i],total + 1))
                ans.pop()
            return res
        
        res = dfs(0,0,0)
        
        return copy
            