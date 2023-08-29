class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        
        mp = defaultdict(int)
        for i in range(height):
            for j in range(width):
                mp[str(i % sideLength) + ',' + str(j % sideLength)] += 1
                
                
        
        #print(mp)
        
        ls = sorted(mp.values(), reverse=True)
        res = 0
        for i in range(maxOnes):
            res += ls[i]
            
        return res