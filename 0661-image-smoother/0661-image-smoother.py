class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        dp = [[0 for i in range(len(img[0]))] for j in range(len(img))]
        
        
        def inbounds(i,j):
            return i >= 0 and i < len(img) and j >= 0 and j < len(img[0])
            
        def checkDirections(i,j):
            count = 0
            score = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if inbounds(i+k,j+l):
                        score += img[i+k][j+l]
                        count += 1
            
            return score // count
        
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                dp[i][j] = checkDirections(i,j)
        
        return dp
                    