class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        rank = defaultdict(lambda:[0] * (len(votes[i]) + 1))
        
        
        for i in range(len(votes)):
            for j in range(len(votes[i])):
                rank[votes[i][j]][j] -= 1
        
        
        res = []
        for val in rank:
            rank[val][len(votes[0])] = val
            heappush(res, rank[val])
        
        #print(res)
        ans = []
        while res:
            arr = heappop(res)
            ans.append(arr[-1])
        
        return ''.join(ans)
            