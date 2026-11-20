from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        # Global counter to track chronological order of tweets
        self.time = 0
        # Maps userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # Maps followerId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # Decrement time so newer tweets have smaller values (for Python's min-heap)
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        min_heap = []
        
        # Combine the user and everyone they follow
        users = self.following[userId] | {userId}
        
        # Push the most recent tweet of each relevant user into the heap
        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                # Store (time, tweetId, userId, next_older_index)
                heapq.heappush(min_heap, (time, tweetId, uid, index - 1))
                
        res = []
        # Extract up to 10 most recent tweets
        while min_heap and len(res) < 10:
            time, tweetId, uid, index = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If that user has older tweets, push the next most recent one
            if index >= 0:
                next_time, next_tweetId = self.tweets[uid][index]
                heapq.heappush(min_heap, (next_time, next_tweetId, uid, index - 1))
                
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].discard(followeeId)
