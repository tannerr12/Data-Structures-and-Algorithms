class FileSharing:

    def __init__(self, m: int):
        self.ids = []
        self.mxId = 1
        self.chunkMap = defaultdict(set)
        self.userMap = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        userId = 0
        
        if self.ids:
            userId = heappop(self.ids)
        else:
            userId = self.mxId
            self.mxId +=1
        
        for val in ownedChunks:
            self.chunkMap[val].add(userId)
            self.userMap[userId].add(val)
        
        return userId
            
    def leave(self, userID: int) -> None:
        heappush(self.ids, userID)
        for val in self.userMap[userID]:
            if userID in self.chunkMap[val]:
                self.chunkMap[val].remove(userID)
        

    def request(self, userID: int, chunkID: int) -> List[int]:
        #print(self.chunkMap)
        #print(self.userMap)
        val = list(self.chunkMap[chunkID])
        val.sort()
        if len(self.chunkMap[chunkID]) > 0:
            self.userMap[userID].add(chunkID)
            self.chunkMap[chunkID].add(userID)
        
        return val


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)