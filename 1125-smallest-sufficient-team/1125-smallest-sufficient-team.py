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
        bitPeople = 2 ** len(people) 
        bitPeople -=1

        memo = {}
        @cache
        def dfs(i,m):
            nonlocal bitmask, bitPeople
            if i >= len(arr) or m == bitmask:
                if m == bitmask:
                    return 0
                
                return bitPeople
            

            res = bitPeople
            
            #dont take
            val = dfs(i+1, m)
            if val.bit_count() < res.bit_count():
                res = val
            
            if arr[i] > 0 and arr[i] & m != arr[i]:
                val = dfs(i+1, m | arr[i]) | (1 << i)
                if val.bit_count() < res.bit_count():
                    res = val
                    
           
            return res
        
        res = dfs(0,0)
        ans = []
 
        for i in range(60):
            if res & (1 << i) > 0:
                ans.append(i)
        
        return ans
            
            