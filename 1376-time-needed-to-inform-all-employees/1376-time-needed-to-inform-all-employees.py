class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            adj[manager[i]].append([i,informTime[manager[i]]])   

        q = deque([[headID,0]])
        res = 0
        while q:
            for i in range(len(q)):
                idx, cost = q.popleft()
                res = max(res, cost)
                for x,c in adj[idx]:
                    q.append([x, c + cost])
        return res