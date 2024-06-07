class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        total = 0
        avail = 0
        
        while numBottles + avail >= numExchange:
            
            avail += numBottles
            total += numBottles
            numBottles = 0
            
            while avail >= numExchange:
                avail -= numExchange
                numBottles += 1
                numExchange += 1
            
            
        
        return total + numBottles
            