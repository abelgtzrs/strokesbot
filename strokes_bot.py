import tweepy
import time
import random

# Your API keys (replace these with your actual keys from the Twitter Developer portal)
API_KEY = 'YB8b7xxeOOMQENnTwOc1XRHVo'
API_SECRET = 'KLJMFf5yERqVNkPckjVFKLFtZkz7Hbef8AwE0SXDQVNRgIZab0'
ACCESS_TOKEN = '1858959756792041472-GxVLlUuHnUFjBBlKTIBDmix1iSnW9u'
ACCESS_TOKEN_SECRET = '304YY7ZFx8nEjrCAMg6Up8WhdsCrk7Lsrm63I9g4lvRcd'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Lyrics and corresponding songs/albums
lyrics_data = [
    {
        "lyric": "Can't you see I'm trying?\nI don't even like it\nI just lied to get to your apartment\nNow I'm staying there just for a while\nI can't think 'cause I'm just way too tired",
        "song": "Is This It",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Is this it?\nIs this it?\nIs this... it?",
        "song": "Is This It",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Said they'd give you anything you ever wanted\nWhen they lied, I knew it was just stable children trying hard not to realize\nI was sitting right behind you",
        "song": "Is This It",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Dear, can't you see? It's them, it's not me\nWe're not enemies, we just disagree\nIf I was like him, all pissed in this bar\nHe changes his mind, says I went too far\nWe all disagree, I think we should disagree, yeah...",
        "song": "Is This It",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Up on a hill, here's where we begin\nThis little story, a long time ago...\nStart to pretend, stop pretending\nIt seems this game is simply never-ending",
        "song": "The Modern Age",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Oh, in the sun, sun, having fun, it's in my blood.\nI just can't help it\nDon't want you here right now, let me go.\nOh, let me g-g-g-g-g-g-g-go...",
        "song": "The Modern Age",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Leaving just in time, stay there for a while\nRolling in the ocean, trying to catch her eye\nWork hard and say it's easy, do it just to please me\nTomorrow will be different, so I'll pretend I'm leaving...",
        "song": "The Modern Age",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I feel so different now, we trained at A-V-A\nI wish you hadn't stayed, my vision's clearer now but I'm unafraid.\nFlying overseas, no time to feel the breeze\nI took too many varieties",
        "song": "The Modern Age",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Soma is what they would take when\nHard times opened their eyes\nSaw pain in a new way\nHigh stakes for a few names\nRacing against sunbeams\nLosing against fig trees\nIn your eyes",
        "song": "Soma",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "And I am\nStop\nAnd go\nIn your eyes\nSee, I am\nStop\nAnd go\nIn your eyes",
        "song": "Soma",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Let's go\n\nWhen I saw her for the first time\nLips moved as her eyes closed\nHeard something in his voice\n\"And I'll be there,\" he says\nThen he walks out\nSomehow he was trying\nToo hard to be like them",
        "song": "Soma",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "And I am\nStop.\nAnd go...\nIn your eyes\nAnd I am\nStop.\nOh, darling let me go",
        "song": "Soma",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Tried it once and they liked it\nAnd tried to hide it\nSays, \"I've been doing this twenty-five years\"\nWell, I'm not listening no more\nAnd these friends, they keep asking for more\nOh, yeah, oh, but that's it",
        "song": "Soma",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I didn't take no shortcuts\nI spent the money that I saved up\nOh, mama running out of luck\nBut like my sister, don't give a fuck",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I wanna steal your innocence\nTo me, my life, it just don't make any sense\nThese strange manners, I love 'em so\nWhy won't you wear your new trenchcoat?",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I should have worked much harder\nI should have just not bothered\nI never show up on weekdays\nAnd something that you learned yesterday",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Drive you to work and you'll be on time\nThese little problems, they're not yours, they're mine\nCome on, listen to what I say\nI've got some secrets that'll make you stay",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I just want to turn you down\nI just want to turn you around\nOh, you ain't never had nothing I wanted, but\nI want it all, I just can't figure out\nNothing...",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "And all together, it went well\nWe may pretend, we were best friends\nThen she said, \"Oh, you're a freak\"\nThey ordered me to make mistakes",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Together again, like the beginning\nIt all works somehow in the end\nThe things we did, the things you hide\nBut for the record, it's between you and I",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I just want to misbehave\nI just want to be your slave\nOh, you ain't never had nothing I wanted, but\nI want it all, I just can't figure out\nNothing...",
        "song": "Barely Legal",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "In many ways, they'll miss the good old days\nSomeday, someday\nYeah, it hurts to say, but I want you to stay\nSometimes, sometimes",
        "song": "Someday",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "When we was young, oh man, did we have fun\nAlways, always\nPromises, they break before they're made\nSometimes, sometimes",
        "song": "Someday",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Oh, Maya says I'm lacking in depth\nI will do my best\nYou say you wanna stand by my side\nDarling, your head's not right",
        "song": "Someday",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "I see alone we stand; together we fall apart\nYeah, I think I'll be alright\nI'm working so I won't have to try so hard\nTables, they turn sometimes\nOh, someday\nNo, I ain't wasting no more time",
        "song": "Someday",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "And now my fears, they come to me in threes\nSo I sometimes\nSay, \"Fate, my friend, you say the strangest things\nI find sometimes\"",
        "song": "Someday",
        "album": "Is This It (2001)"
    },
        {
        "lyric": "No choice now, it's too late\nLet him go, he gave up\nI gave up",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Lisa said, \"Take time for me\"\nDropping him down to his knees\nAh, chest down",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Take me away\nSee I've got to explain\nThings, they have changed\nIn such a permanent way",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Life seems unreal\nCan we go back to your place?\nOh, \"You drink too much\"\nMakes me drink just the same",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "People tried. Felt so right\nGiving themselves good advice\nLooking down sometimes felt nice",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "He knows it's justified to kill to survive\nHe then, in dollars, makes more dead than alive\nLet's suck more blood, let's run three hours a day",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "The world is over but I don't care\n'Cause\nI am with you\nNow I've got to explain\nThings, they have changed\nIn such a permanent way",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "Life seems unreal\nCan we go back to your place?\n\"You drink too much\"\nMakes me drink just the same",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
    {
        "lyric": "The first time, it happened too fast\nThe second time, I thought it would last\nWe all like it a little different",
        "song": "Alone Together",
        "album": "Is This It (2001)"
    },
        ]

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

#Client ID: RVQxdXZ0dHFyaTVKaFVMc2I2SVU6MTpjaQ+
#Client Secret: J4PlnTdlFi_H1ZxBCQIaXIbFt0XjOLLzRc-phF8fZY5YH-uMeQ