# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def isGood(mid):
            total = 0
            for val in text:
                total += fontInfo.getWidth(mid, val)
                
                if total > w:
                    return False
            
            return True
        
        l,r = 0, len(fonts) -1
        res =-1
        while l <= r:
            
            mid = (l+r) //2
            if fontInfo.getHeight(fonts[mid]) <= h and isGood(fonts[mid]):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
                
        
        return res if res == -1 else fonts[res]
                