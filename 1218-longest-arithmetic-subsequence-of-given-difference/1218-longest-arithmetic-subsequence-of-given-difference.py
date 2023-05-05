class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        mp = defaultdict(int)
        opp = difference * -1
        for i, v in enumerate(arr):
            mp[v] = max(1, mp[v + opp] + 1)
            
        
        return max(mp.values())
            
            