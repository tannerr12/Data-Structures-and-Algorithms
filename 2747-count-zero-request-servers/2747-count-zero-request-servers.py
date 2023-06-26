class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        for i in range(len(queries)):
            
            queries[i] = [queries[i], i]
        
        queries.sort()
        
        logs = sorted(logs, key=lambda x:(x[1], x[0]))
        s = set()

        left = 0
        right = 0
        c = Counter()
        
        ans = [0] * len(queries)
        
        for i in range(len(queries)):
            
            while left < len(logs) and logs[left][1] < queries[i][0] - x:
                c[logs[left][0]] -=1
                if c[logs[left][0]] == 0:
                    del c[logs[left][0]]
                left +=1
            
            #print(c)
            while right < len(logs) and logs[right][1] <= queries[i][0]:
                c[logs[right][0]] +=1
                if c[logs[right][0]] == 0:
                    del c[logs[right][0]]
                right +=1
            
            #print(c)
            ans[queries[i][1]] = n - len(c)
        
        return ans
            
            