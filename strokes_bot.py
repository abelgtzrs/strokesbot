import tweepy
import time
import random
from keys import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN
from lyrics import lyrics_data


# Authenticate to Twitter
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def tweet_lyrics():
    while True:
        # Select a random lyric
        lyric_data = random.choice(lyrics_data)
        lyric = lyric_data["lyric"]
        song = lyric_data["song"]
        album = lyric_data["album"]
        
        # Tweet the lyric
        tweet = api.update_status(lyric)
        
        # Reply with song name and album
        api.update_status(f"This is from '{song}' on the album '{album}'.", in_reply_to_status_id=tweet.id)
        
        # Wait 30 minutes
        time.sleep(1800)  # 1800 seconds = 30 minutes

if __name__ == "__main__":
    tweet_lyrics()
