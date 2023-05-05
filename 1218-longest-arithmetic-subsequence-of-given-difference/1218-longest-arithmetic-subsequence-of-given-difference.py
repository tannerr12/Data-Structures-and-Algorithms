class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        mp = defaultdict(int)
        for i, v in enumerate(arr):
            mp[v] = max(1, mp[v - difference] + 1)

        return max(mp.values())
            
            