import os
import logging
import tweepy
from model import NGO 

ConsumerKey = os.getenv('TWITTER_CONSUMER_KEY', None)
ConsumerSecret = os.getenv('TWITTER_CONSUMER_SECRET', None)
AccessKey = os.getenv('TWITTER_ACCESS_TOKEN_KEY')
AccessSecret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

Tejal = '78686298'
Shabnam = '281702049'

logging.basicConfig()
logger = logging.getLogger("engine")

def initiate_dm(ngo_rep, victim_id, key, secret):
  logger = logging.getLogger("engine")
  auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
  auth.set_access_token(AccessKey, AccessSecret)
  api = tweepy.API(auth)
  text = 'D {0} Follow {1}. He/She is your system assigned representative.'.format(victim_id, ngo_rep)
  api.send_direct_message(user_id=victim_id, text=text)
  logger.info('Sent {0} to {1}'.format(text, victim_id))

  # Todo Fetch the tokens for ngo from database
  auth.set_access_token(key, secret)
  api = tweepy.API(auth)
  api.create_friendship(victim_id)
  api.send_direct_message(user_id=victim_id, text=text)


def get_ngo(victim_id, location):
  ngo = NGO.query.filter_by(location=location).first()
  initiate_dm(ngo.twitter_handle, ngo.twitter_user_id, victim_id)
  
if __name__ == "__main__":
  initiate_dm(Shabnam, Tejal, '', '')
