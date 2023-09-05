# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        
        #divide each quadrant into 4 more quandrants if a ship is found and keep going until no more ships are found in a quadrant.
        #count unique quadrants found, this is simmilar to quadtree
        
        @cache
        def divide(x,y):
            
            if not sea.hasShips(y,x):
                return 0
            if abs(x.x - y.x) + abs(x.y - y.y) <= 1:
                return 1
        
            #divide the current square into 4 
            res = 1
            
            midX = (x.x + y.x) / 2
            midY = (x.y + y.y) / 2
            midY -= 0.1
            midX -= 0.1
            topleft = divide(Point(x.x, midY),Point(midX, y.y))
            topright = divide(Point(midX, midY),Point(y.x, y.y))
            botleft = divide(Point(x.x, x.y), Point(midX, midY))
            botright = divide(Point(midX, x.y), Point(y.x, midY))
            
            res = max(res, topleft + topright + botleft + botright)
            
            return res
        
        
        
        return divide(bottomLeft, topRight)