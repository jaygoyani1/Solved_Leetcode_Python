class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.journey = collections.defaultdict(lambda : [0,0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time = self.check_in.pop(id)
        self.journey[(start,stationName)][0] += (t-time)
        self.journey[(start,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, trips = self.journey[(startStation,endStation)]
        return time/trips
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)