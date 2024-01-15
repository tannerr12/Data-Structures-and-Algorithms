class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        
        for win,lose in matches:
            
            count[win] += 0
            count[lose] += 1
            
        ans = []
        res1 = []
        res2 = []
        
        for key,val in sorted(count.items()):
            
            if val == 0:
                res1.append(key)
            if val == 1:
                res2.append(key)
                
        
        ans.append(res1)
        ans.append(res2)
        return ans