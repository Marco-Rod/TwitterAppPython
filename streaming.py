import tweepy
from tweepy import Stream
#from main import TwitterAPI
from tweepy.streaming import StreamListener
import credentials


__consumer_key= credentials.CONSUMER_KEY
__consumer_secret= credentials.CONSUMER_SECRET
__access_token=credentials.ACCESS_TOKEN
__access_token_secret=credentials.ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(__consumer_key, __consumer_secret)
auth.set_access_token(__access_token, __access_token_secret)
api = tweepy.API(auth)


class Mylistener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error on_datSa: %s' % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True
#auth=TwitterAPI.main()
twitter_stream = Stream(auth=api, listener=Mylistener())
twitter_stream.filter(track=['#python'])