class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        mp = defaultdict(set)
        for x,y in logs:
            mp[x].add(y)
            

        for key,val in mp.items():
            ans[len(val) -1] += 1
        
        return ans
            