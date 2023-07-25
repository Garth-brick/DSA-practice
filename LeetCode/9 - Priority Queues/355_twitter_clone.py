import collections
import heapq
from typing import List


class Tweet:

    def __init__(self, tweetId, time):
        self.tweetId = tweetId
        self.time = time

    def __lt__(self, other):
        # when ordering tweets, we want to order them by the time at which they were posted
        return self.time < other.time
    
    def __repr__(self):
        return f"{self.time}: #{self.tweetId}"


class Twitter:

    def __init__(self):

        # {userId: [Tweets]}
        # the tweets will be in a queue of length 10 because we will never need to access more than 10 tweets
        self.tweetList = {}

        # {userId: {Followees}}
        # keeping the followee IDs in a set because they have to be unique
        self.followerList = {}

        # keeping track of time, will be incremented everytime a tweet is posted
        self.time = 0

        # keeping this constant in one place 
        self.feedSize = 10


    def postTweet(self, userId: int, tweetId: int) -> None:

        # if the user has never posted a tweet
        if userId not in self.tweetList:
            self.tweetList[userId] = collections.deque()

        # adding this new tweet to this user's list of tweets
        # we want to keep this as the first tweet in that list because its the most recent one
        newTweet = Tweet(tweetId, self.time)
        userTweetList = self.tweetList[userId]
        userTweetList.appendleft(newTweet)

        # popping from the other side if there are more than 10 tweets now
        if len(userTweetList) > self.feedSize:
            userTweetList.pop()

        # incrementing the time for the next tweet
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # making sure that this user follows themself
        self.follow(userId, userId)

        followedUserIds = self.followerList[userId]

        resultHeap = []
        for followedUserId in followedUserIds:
            # if a followedUser has never posted a tweet then move on to the next followed user
            if followedUserId not in self.tweetList:
                continue
            tweets = self.tweetList[followedUserId]
            for tweet in tweets:
                if len(resultHeap) == self.feedSize and tweet.time < resultHeap[0]:
                    # if we have 10 tweets and reached far enough into the queue that the tweet times are less than our oldest tweet then there's no point checking more tweets in this queue
                    break
                heapq.heappush(resultHeap, tweet)
                while len(resultHeap) > self.feedSize:
                    # this will remove the tweet with the lowest time as soon as we have more than 10 tweets
                    heapq.heappop(resultHeap)

        resultList = collections.deque()
        actualFeedSize = len(resultHeap)
        for i in range(actualFeedSize):
            resultList.appendleft(heapq.heappop(resultHeap).tweetId)
        return list(resultList)

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # "followerId" starts following the "followeeId"

        # adding this to the map if it doesn't exist
        if followerId not in self.followerList:
            self.followerList[followerId] = set()
        
        # adding the new Id to the set (if duplicate then set will discard anyway)
        self.followerList[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # the "followerId" will unfollow the "followeeId"

        # making sure that this followerId exists
        if followerId not in self.followerList:
            return
        
        # using "discard" instead of "remove" to avoid getting an error if the followeeId isn't present
        self.followerList[followerId].discard(followeeId)
        


obj = Twitter()
obj.postTweet(2,5)
obj.follow(1,2)
param_2 = obj.getNewsFeed(1)
print(param_2)
# obj.unfollow(followerId,followeeId)