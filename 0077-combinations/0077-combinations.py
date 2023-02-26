class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ls = []
        for i in range(1, n+1):
            ls.append(i)
        comb = combinations(ls, k)
        return comb