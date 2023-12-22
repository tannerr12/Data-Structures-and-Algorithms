from collections import defaultdict
from typing import List

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        rank = [0] * (m + n)  # Combined rank for rows and columns

        # Map each value to its coordinates
        value_to_positions = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_to_positions[matrix[i][j]].append((i, j))

        # Process each value in sorted order
        for value in sorted(value_to_positions):
            positions = value_to_positions[value]
            rank2 = rank.copy()
            parent = list(range(m + n))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            for i, j in positions:
                i, j = find(i), find(j + m)
                parent[i] = j
                rank2[j] = max(rank2[i], rank2[j])

            for i, j in positions:
                rank[i] = rank[j + m] = matrix[i][j] = rank2[find(i)] + 1

        return matrix
