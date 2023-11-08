class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        def update(biTree, idx, val):
            while idx < len(biTree):
                biTree[idx] += val
                idx += lsb(idx)

        def prefixSum(biTree, idx):
            total = 0
            while idx > 0:
                total += biTree[idx]
                idx -= lsb(idx)
            return total

        def lsb(n):
            return n & -n

        # Create BIT with size 2*m+1
        biTree = [0] * (2*m + 1)
        res = []
        dict = {}

        # Start biTree build from m-th position, i.e., [m to 2*m]
        # Set 1 for each index, so we can query prefixSum, which will give the number of elements before
        # O(m*log(m))
        for i in range(1, m+1):
            dict[i] = i+m
            update(biTree, i+m, 1)

        # For each query
        #   Find the index of the number using dict
        #   Then find prefixSum, which is the number of elements before that element
        #   Update current index to -1, like removing that number from that index
        #   Move that number to m-1 (start-1 index of current biTree)
        # O(n * (log(m) + log(m)))
        for query in queries:
            idx = dict[query]
            res.append(prefixSum(biTree, idx) - 1)
            update(biTree, idx, -1)
            update(biTree, m, 1)
            dict[query] = m
            m -= 1

        return res


