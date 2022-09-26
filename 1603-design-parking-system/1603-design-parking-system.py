class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.b = big
        self.m = medium
        self.s = small

    def addCar(self, carType: int) -> bool:
        
        if carType == 1:
            if self.b == 0:
                return False
            
            self.b -=1
            
            
        
        elif carType == 2:
            if self.m == 0:
                return False
            
            self.m -=1
            
        
        elif carType == 3:
            if self.s == 0:
                return False
            
            self.s -=1
            
        
        
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)