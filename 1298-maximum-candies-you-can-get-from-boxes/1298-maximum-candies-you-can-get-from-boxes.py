class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:


        q = deque()
        boxes = set()
        for i in range(len(initialBoxes)):
            q.append(initialBoxes[i])
            boxes.add(initialBoxes[i])

        key = set()
        seen = set()
        res = 0
        while q:
            for i in range(len(q)):

                node = q.popleft()

                if (
                    node in seen
                    or node not in boxes
                    or (status[node] == 0 and node not in key)
                ):
                    continue

                seen.add(node)

                res += candies[node]

                for val in containedBoxes[node]:
                    boxes.add(val)
                    if (
                        val not in seen
                        and (val in boxes and val in key)
                        or status[val] == 1
                    ):
                        q.append(val)

                for val in keys[node]:
                    key.add(val)
                    if (
                        val not in seen
                        and (val in boxes and val in key)
                        or status[val] == 1
                    ):
                        q.append(val)

        return res


# @lc code=end
