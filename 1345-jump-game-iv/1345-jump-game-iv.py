class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        """
        nxt = defaultdict(list)
        
        dp = [0] * len(arr)
        heappush(nxt[arr[-1]],(0,len(arr) -1))
        for i in range(len(arr)-2,-1,-1):
            val = float('inf')
            if arr[i] in nxt and len(nxt[arr[i]]) > 0:
                val = min(val,nxt[arr[i]][0][0] + 1)
            
            val = min(val, dp[i+1] + 1)
            heappush(nxt[arr[i]],(val,i))
            dp[i] = val
        
        
        
        nxt = defaultdict(list)
        heappush(nxt[arr[-1]],(0,len(arr) -1))
        for i in range(len(arr)-1,0,-1):
            val = float('inf')
            if arr[i] in nxt and len(nxt[arr[i]]) > 0:
                val = min(val,nxt[arr[i]][0][0] + 1)
            
            val = min(dp[i], dp[i-1] +1)
            heappush(nxt[arr[i]],(val,i))
            dp[i] = val
        
        
        
        #print(nxt[68])
        val = float('inf')
        if arr[0] in nxt and len(nxt[arr[0]]) > 0:
            val = min(val,nxt[arr[0]][0][0] + 1)
            
        dp[0] = min(dp[0],val)
        print(dp)
        return dp[0]
        """
        lookup = defaultdict(list)
        for i in range(len(arr)):
            lookup[arr[i]].append(i)
            
        best = [float('inf')] * len(arr)
        best[0] = 0
        q = deque()
        q.append(0)
        N = len(arr)
        done = set()
        while q:
            
            for i in range(len(q)):
                current = q.popleft()
                if current == N - 1:
                    return best[current]
                
                for x in [current-1, current+1]:
                    if 0 <= x < N and best[current] + 1 < best[x]:
                        q.append(x)
                        best[x] = best[current] + 1
                
                #visit each number once
                if arr[current] not in done:
                    done.add(arr[current])
                    
                    for x in lookup[arr[current]]:
                        if best[current] + 1 < best[x]:
                            q.append(x)
                            best[x] = best[current] + 1
        return -1