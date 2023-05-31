class UndergroundSystem:

    def __init__(self):
        self.people = {}
        self.station = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.people:
            self.people[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.people:
            time,st = self.people[id]
            
            if (st,stationName) in self.station:
                x,y = self.station[(st,stationName)] 
                x += t-time
                y+=1

                self.station[(st,stationName)] = (x,y)
            else:
                self.station[(st,stationName)] = (t-time, 1)
            
            del self.people[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        val,mult = self.station[(startStation,endStation)]

        return val / mult


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)