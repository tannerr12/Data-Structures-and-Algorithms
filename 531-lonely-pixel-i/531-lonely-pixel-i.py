class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        rdp = collections.defaultdict(int)
        
        cdp = collections.defaultdict(int)
        res = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                
                if picture[r][c] == 'B':
                    rdp[r] +=1
                    cdp[c] +=1
                    
        
        
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    if rdp[r] == 1 and cdp[c] == 1:
                        res +=1
        
        return res