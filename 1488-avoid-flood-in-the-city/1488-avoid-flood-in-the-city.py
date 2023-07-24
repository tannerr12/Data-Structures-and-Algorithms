class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        nxt = {}
        nxtFlood = [-1] * len(rains)
        for i in range(len(rains) -1,-1,-1):
            if rains[i] == 0:
                continue
            if rains[i] in nxt:
                nxtFlood[i] = nxt[rains[i]]
                nxt[rains[i]] = i
            else:
                nxt[rains[i]] = i
        
        dry = []
        ans = [-1] * len(rains)
        lake = Counter()
        for i in range(len(rains)):
            if nxtFlood[i] > -1:
                heappush(dry, (nxtFlood[i],i))
            if rains[i] > 0:
                if lake[rains[i]] > 0:
                    return []
                    
                else:
                    lake[rains[i]] = 1
            else:
                if dry:
                    val, idx = heappop(dry)
                    ans[i] = rains[idx]
                    lake[rains[idx]] = 0
                else:
                    ans[i] = 1
        
        
        return ans