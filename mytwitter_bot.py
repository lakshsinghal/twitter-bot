import tweepy
import time

CONSUMER_KEY = 'pIbiVt7M2NdJat1THXGZgegqK'
CONSUMER_SECRET = 'cluWtJNT276oPC5vxBQcbB6WhSCFgIzjbknUG2taEAWmRQyAWe'
ACCESS_KEY = '841339024933548032-kM279cAVG7yc6jgavbyxrPDHtCsRLOL'
ACCESS_SECRET = 'KvkfYyKykZyJFJOkMRlw2R623z6kgpvr522Em0Patelbj'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

print('This is my Twitter Bot. Yayyy!')

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_tweets():
     print('retrieving and replying to tweets...', flush=True)
         # DEV NOTE: use 1060651988453654528 for testing.
     last_seen_id = retrieve_last_seen_id(FILE_NAME)
         # NOTE: We need to use tweet_mode='extended' below to show
         # all full tweets (with full_text). Without it, long tweets
         # would be cut off.
     mentions = api.mentions_timeline(
                             last_seen_id,
                             tweet_mode='extended')
     for mention in reversed(mentions):
          print(str(mention.id) + ' - ' + mention.full_text, flush=True)
          last_seen_id = mention.id
          store_last_seen_id(last_seen_id, FILE_NAME)
          if '#hey' in mention.full_text.lower():
               print('found #hey!')
               print('responding the awesome guy back...')
               api.update_status('@' + mention.user.screen_name + '  #Heyman How ya doin? See you soon!:)))  n'+ str(mention.id))

          elif '#weather' in mention.full_text.lower():
               print('found #weather!')
               print('responding about the weather...')
               api.update_status('@' + mention.user.screen_name + '  Did you check the weather forecast today? ''cause it can rain anytime   \n'+ str(mention.id))

          elif '#hello' in mention.full_text.lower():
               print('found #hello!')
               print('responding the awesome guy back...')
               api.update_status('@' + mention.user.screen_name + '  Hi! Good to see you around here. \n '+ str(mention.id))

          elif '#food' in mention.full_text.lower():
               print('found #food!')
               print('responding about the food...')
               api.update_status('@' + mention.user.screen_name + '  You hungry dude? Here, have some tweets.   \n'+ str(mention.id))

          elif '#bye' in mention.full_text.lower():
               print('found #bye')
               print('responding about the bye...')
               api.update_status('@' + mention.user.screen_name + '  Hit me up anytime. See yaa...   \n'+ str(mention.id))

          elif '#talk' in mention.full_text.lower():
               print('found #talk')
               print('responding about the "TALK"...')
               api.update_status('@' + mention.user.screen_name + '  You think I''m real? Tis'' confusion!!   \n'+ str(mention.id))

          elif '#bot' in mention.full_text.lower():
               print('found #bot')
               print('responding about the BOT...')
               api.update_status('@' + mention.user.screen_name + '  I''m a real life human bring. Hit me up on snapchat, if you ain''t a bot!   \n'+ str(mention.id))

          elif '#game' in mention.full_text.lower():
               print('found #game')
               print('responding about the game...')
               api.update_status('@' + mention.user.screen_name + '  IT ISN''T A GAME ANYMORE. MORIARTY! - Holmes   \n'+ str(mention.id))
               
          elif '#play' in mention.full_text.lower():
               print('found #play')
               print('responding about the play...')
               api.update_status('@' + mention.user.screen_name + '  Let''s play. Talk to me in hashtags.####TALK####   \n'+ str(mention.id))

          else:
              break


while True:
     reply_tweets()
     time.sleep(10)
