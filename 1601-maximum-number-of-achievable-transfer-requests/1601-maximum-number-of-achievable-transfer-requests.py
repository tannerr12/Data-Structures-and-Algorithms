class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        people = defaultdict(int)
        def dfs(i):

            if i >= len(requests):
                if all(v == 0 for v in people.values()):
                    return 0
                return float('-inf')

            res = float('-inf')
            # ignore request
            res = max(res, dfs(i+1))

            # take request
            x,y = requests[i]
            prevx = people[x]
            prevy = people[y]

            people[x] -= 1
            people[y] += 1

            if people[x] == 0:
                del people[x]
            if people[y] == 0:
                del people[y]
                
            res = max(res, dfs(i+1) + 1)

            people[x] = prevx
            people[y] = prevy

            return res

        return dfs(0)
