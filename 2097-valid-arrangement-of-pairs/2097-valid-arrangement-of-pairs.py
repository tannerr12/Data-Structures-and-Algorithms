from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            in_degree[end] += 1
            out_degree[start] += 1

        start = pairs[0][0]
        for node in out_degree:
            if out_degree[node] - in_degree[node] == 1:
                start = node
                break

        ans = []
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            ans.append(node)

        dfs(start)
        ans = [[ans[i + 1],ans[i]] for i in range(len(ans) - 1)]
        return ans[::-1]

