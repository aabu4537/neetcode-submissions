class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [userId, tweetId]
        self.tweets.append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        n = len(self.tweets) -1
        news = []
        while n >= 0 and len(news) <10:
            t = self.tweets[n]
            uid = t[0]
            tid = t[1]
            if uid in self.follows[userId] or uid == userId:
                news.append(tid)
            n = n-1
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

