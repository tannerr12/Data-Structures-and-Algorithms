class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        serverheap = []
        serverq = []
        for i in range(len(servers)):
            heappush(serverq, (servers[i], i))
            
        ans = [0] * len(tasks)
        for i in range(len(tasks)):
            while serverheap and serverheap[0][0] <= i:
                t,w,j = heappop(serverheap)
                heappush(serverq,(w,j))
                
            if len(serverq) > 0:
                w,j = heappop(serverq)
                ans[i] = j
                heappush(serverheap, (i + tasks[i], w, j))
            else:
                t,w,j = heappop(serverheap)
                ans[i] = j
                heappush(serverheap, (t + tasks[i],w,j))

        return ans
            
            
        