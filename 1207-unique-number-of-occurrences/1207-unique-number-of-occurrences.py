class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = Counter(arr)
        s = set(h.values())
        
        return len(s) == len(h)
        
        
        