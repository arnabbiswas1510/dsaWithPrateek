"""
https://leetcode.com/problems/tweet-counts-per-frequency/


"""
import bisect
from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self.a = defaultdict(list) #Map of tweet and list of times it came in

    def recordTweet(self, tn, time):
        bisect.insort(self.a[tn], time)

    def getTweetCountsPerFrequency(self, freq, tn, startTime, endTime):
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        i = startTime
        res = []
        while i <= endTime:
            j = min(i + delta, endTime+1)
            res.append(bisect.bisect_left(self.a[tn], j) - bisect.bisect_left(self.a[tn], i)) #bisect_left returns the
            # leftmost position of the element in sorted array in case the element is repeated n the array.
            # bisect_right returns rightmost. If element is not repeated they both return same value
            i += delta
        return res

tweetCounts=TweetCounts()
tweetCounts.recordTweet("tweet3", 0)                              # New tweet "tweet3" at time 0
tweetCounts.recordTweet("tweet3", 60)                             # New tweet "tweet3" at time 60
tweetCounts.recordTweet("tweet3", 10)                             # New tweet "tweet3" at time 10
print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59)) # return [2]; chunk [0,59] had 2 tweets
print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60)) # return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
tweetCounts.recordTweet("tweet3", 120)                            # New tweet "tweet3" at time 120
print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))  # return [4]; chunk [0,210] had 4 tweets