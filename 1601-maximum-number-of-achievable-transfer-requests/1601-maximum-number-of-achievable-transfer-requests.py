class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        people = defaultdict(int)
        #requests.sort()
        def dfs(i):
            
            if i >= len(requests):
                
                if len(people) == 0:
                    return 0
                return float('-inf')
            
            res = float('-inf')
            #ignore request
            res = max(res, dfs(i+1))
            
            #take request

            x,y = requests[i]
            prevx = people[x]
            prevy = people[y]
            
            people[x] -=1
            people[y] +=1
            
            if x in people and people[x] == 0:
                del people[x]
            if y in people and people[y] == 0:
                del people[y]
            res = max(res, dfs(i+1) + 1)
            
            people[x] = prevx
            people[y] = prevy
            
            if x in people and people[x] == 0:
                del people[x]
            if y in people and people[y] == 0:
                del people[y]
            
            return res
            
        
        res = dfs(0)
        
        if res == float('-inf'):
            return 0
        else:
            return res
            
            