import argparse
import tweepy
import struct

from datetime import datetime
from loguru import logger

class TweetsReceiver(object):
    """Fetch tweets"""

    def __init__(self):
        list_words = list()
        

    def getTweets(self, words, qtd):

        TWEETS_FORMAT = 'I200s1120s800sdI'

        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--output-dir', default='data', help='output directory')
        parser.add_argument('-f', '--from', required=False, help='timestamp from where to start the query')

        ARGS = parser.parse_args()


        auth = tweepy.OAuthHandler('TOKEN', 'TOKEN')
        auth.set_access_token('TOKEN', 'TOKEN')
        api = tweepy.API(auth)

        list_words = words
        tweets = tweepy.Cursor(api.search, q=list_words, lang='en').items(qtd)               

        return tweets

            # rec = (1, 'test 1'.encode('utf-8'), 'aaadddd'.encode('utf-8'), 'test 3'.encode('utf-8'), datetime.utcnow().timestamp(), 5)
            # b = struct.pack(TWEETS_FORMAT, *rec)
            # logger.debug(b)
            # logger.debug(len(b))


