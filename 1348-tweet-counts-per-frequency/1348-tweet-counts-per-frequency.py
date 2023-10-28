class TweetCounts:

    def __init__(self):
        self.mp = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        
        insort(self.mp[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            inter = 60
        elif freq == 'hour':
            inter = 3600
        else:
            inter = 86400
        ans = []
        start = bisect_left(self.mp[tweetName], startTime)
        #print(self.mp)
        for i in range(startTime, endTime+1, inter):
            
            end = bisect_right(self.mp[tweetName], min(i + inter -1, endTime)) 
            ans.append(end - start)
            start = end
        
        return ans
            
            
            

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)