import tweepy
import time

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():

  cfg = { 
    "consumer_key"        : "value",
    "consumer_secret"     : "value",
    "access_token"        : "value",
    "access_token_secret" : "value" 
    }
  api = get_api(cfg)
  f = open("mahts.txt",'w')

  for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    f.write(follower.screen_name)
 
  f = open('hello.txt')
  for line in f:
    line2 = "@krizzGames "+line
    status = api.update_status(status=line2)
    print(line," Tweet sent.")
    time.sleep(10)

if __name__ == "__main__":
  main()
