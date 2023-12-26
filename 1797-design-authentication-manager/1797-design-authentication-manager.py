class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive        
        self.tokenTime = {}
        self.heap = []
        self.heapSub = []
    def generate(self, tokenId: str, currentTime: int) -> None:
        heappush(self.heap, currentTime + self.ttl)
        self.tokenTime[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenTime and self.tokenTime[tokenId] > currentTime:
            heappush(self.heapSub, self.tokenTime[tokenId])
            self.tokenTime[tokenId] = currentTime + self.ttl
            heappush(self.heap, currentTime + self.ttl)
            
    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.heapSub and self.heapSub[0] <= currentTime:
            heappop(self.heapSub)
        while self.heap and self.heap[0] <= currentTime:
            heappop(self.heap)
        
        return len(self.heap) - len(self.heapSub)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)