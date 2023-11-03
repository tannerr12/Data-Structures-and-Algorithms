class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        idx = 0
        ans = []
        count = 0
        while idx < len(target):
            
            diff = target[idx] - count - 1
            
            ans = ans + (['Push', 'Pop'] * diff)
            ans.append('Push')
            count = target[idx]
            
            idx += 1
        
        
        return ans