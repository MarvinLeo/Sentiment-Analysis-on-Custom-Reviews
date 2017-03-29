from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sentiment as sent

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data['text']
        attitude, confidence = sent.sentiment(tweet)

        print tweet
        print attitude, confidence
        # if confidence * 100 >= 80:
        #     output = open("twitter-out.txt", "a")
        #     output.write(attitude)
        #     output.write('\n')
        #     output.close()
        return True

    def on_error(self, status):
        print status

def readTweet(ckey, csecret, atoken, asecret, keyword):
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[keyword])