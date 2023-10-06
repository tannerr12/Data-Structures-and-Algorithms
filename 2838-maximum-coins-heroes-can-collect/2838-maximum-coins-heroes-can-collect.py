class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        
        moncoin = []
        for x,y in zip(monsters,coins):
            moncoin.append((x,y))
            
        
        moncoin.sort()

        for i in range(len(heroes)):
            heroes[i] = (heroes[i], i)
            
            
        heroes.sort()
        
        
        ans = [0] * len(heroes)
        
        idx = 0
        
        cur = 0
        for i in range(len(heroes)):
            
            while idx < len(moncoin) and heroes[i][0] >= moncoin[idx][0]:
                cur += moncoin[idx][1]
                idx += 1
            
            ans[heroes[i][1]] = cur
        
        
        return ans
            
            