class Video:
    
    def __init__(self, Id, video):
        
        self.videoId = Id
        self.likes = 0
        self.dislikes = 0
        self.video = video
        self.views = 0
        
class VideoSharingPlatform:

    def __init__(self):
        self.h = {}
        self.heap = [i for i in range((10**5) + 1)]
        

    def upload(self, video: str) -> int:
        
        
        Id = heappop(self.heap)
        v = Video(Id,video)
        self.h[Id] = v
        
        return Id

    def remove(self, videoId: int) -> None:
        if videoId in self.h:
            heappush(self.heap, videoId)
            del self.h[videoId]
        

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.h:
            return '-1'
        v = self.h[videoId].video
        self.h[videoId].views +=1
        return v[startMinute:endMinute +1]
        

    def like(self, videoId: int) -> None:
        if videoId in self.h:
            self.h[videoId].likes +=1

    def dislike(self, videoId: int) -> None:
        if videoId in self.h:
            self.h[videoId].dislikes +=1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.h:
            v = self.h[videoId]
        
            return [v.likes, v.dislikes]
        return [-1]
    def getViews(self, videoId: int) -> int:
        if videoId in self.h:
            return self.h[videoId].views
        return -1

# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)