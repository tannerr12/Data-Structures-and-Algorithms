class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        rdp = collections.defaultdict(list)
        
        cdp = collections.defaultdict(list)
        res = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                
                if picture[r][c] == 'B':
                    rdp[r].append('B')
                    cdp[c].append('B')
                    
        
        
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    if len(rdp[r]) == 1 and len(cdp[c]) == 1:
                        res +=1
        
        return res