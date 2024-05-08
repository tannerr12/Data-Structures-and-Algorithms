class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        mp = defaultdict(int)
        
        for i in range(len(score)):
            mp[score[i]] = i
            
        score.sort(reverse=True)
        
        ans = [''] * len(score)
        
        for i in range(len(score)):
            if i == 0:
                ans[mp[score[i]]] = 'Gold Medal'
            elif i == 1:
                ans[mp[score[i]]] = 'Silver Medal'
            elif i == 2:
                ans[mp[score[i]]] = 'Bronze Medal'
            else:
                ans[mp[score[i]]] = str(i+1)
        
        
        return ans
            