class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        def search(i):
            
            l = 0
            r = count[i] - 1
            res = 0
            while l <= r:
                
                mid = (l + r) // 2
                
                m = money[i] + (sell[i] * mid)
                
                res = max(res, min(count[i] - mid, m // upgrade[i]))
                
                if (m // upgrade[i]) > count[i] - mid:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return res
                
                
        
        ans = [0] * len(count)
        for i in range(len(count)):
            ans[i] = search(i)
        
        
        return ans