class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = Counter(arr)
        s = set()
        
        
        for val in h.values():
            if val in s:
                return False
            s.add(val)
        
        return True