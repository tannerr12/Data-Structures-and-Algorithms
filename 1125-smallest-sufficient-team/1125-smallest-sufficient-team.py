class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        n = len(people)
        m = len(req_skills)
        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]
        dp = [-1] * (1 << m)
        dp[0] = 0

        
        
        def dfs(m):
            if dp[m] != -1:
                return dp[m]
            
            for i in range(len(people)):
                nm = m & ~skills_mask_of_person[i]
                if nm != m:
                    pm = dfs(nm) |  (1 << i)
                    if (dp[m] == -1 or
                        pm.bit_count()
                       < dp[m].bit_count()):
                        dp[m] = pm
                    
            return dp[m]
        res = dfs((1 << m) -1)
        ans = []
        for i in range(len(people)):
            if res & (1 << i) > 0:
                ans.append(i)
                
        return ans
            
            